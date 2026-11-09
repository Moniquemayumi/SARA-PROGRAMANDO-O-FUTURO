import time
import unittest
import app

class TesteIntegracaoSARA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.app.test_client()
        app.app.testing = True

        # Cria ou obtém um usuário de teste
        with app.app.app_context():
            u = app.Usuario.query.filter_by(login='mariana.alves').first()
            if not u:
                u = app.Usuario(
                    nome='Mariana Alves',
                    email='mariana.alves@exemplo.com',
                    login='mariana.alves',
                    senha='123',
                    area='Tecnologia',
                    tipo='vitima'
                )
                app.db.session.add(u)
                app.db.session.commit()
            app.usuario_logado_id = u.id
            cls.usuario_padrao_id = u.id

    def test_01_home_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'SARA', res.data)
        self.assertIn(b'Sistema de Apoio e Registro de Ass', res.data)

    def test_01_demo_reports_are_clearly_fictional_and_detailed(self):
        res = self.client.get('/?demo=1')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Localidade fict\xc3\xadcia', res.data)
        self.assertIn(b'n\xc3\xa3o representam organiza\xc3\xa7\xc3\xb5es, pessoas ou den\xc3\xbancias reais', res.data)
        self.assertIn(b'Ver detalhes do cen\xc3\xa1rio fict\xc3\xadcio', res.data)
        self.assertIn(b'A lideran\xc3\xa7a combina prioridades por escrito e encontros peri\xc3\xb3dicos', res.data)
        self.assertNotIn(b'Ponte Norte Tecnologia', res.data)
        self.assertNotIn(b'Horizonte Log\xc3\xadstica', res.data)

    def test_02_login_get(self):
        res = self.client.get('/login')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Acesse sua conta', res.data)
        self.assertIn(b'name="login"', res.data)
        self.assertIn(b'name="senha"', res.data)

    def test_03_cadastrar_get(self):
        res = self.client.get('/cadastrar')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Cadastre-se na SARA', res.data)
        self.assertIn(b'name="email"', res.data)
        self.assertIn(b'name="area"', res.data)

    def test_04_cadastrar_post(self):
        unique_suffix = int(time.time() * 1000)
        data = {
            'nome': f'Usuaria Teste {unique_suffix}',
            'email': f'teste_{unique_suffix}@sara.org',
            'login': f'login_{unique_suffix}',
            'senha': 'senha_valida_123',
            'area': 'Tecnologia',
            'tipo': 'vitima'
        }
        res = self.client.post('/cadastrar', data=data, follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, '/')
        self.assertIsNotNone(app.usuario_logado_id)

    def test_05_denunciar_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        res = self.client.get('/denunciar')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Quebre o sil', res.data)
        self.assertIn(b'action="/nova_denuncia"', res.data)

    def test_06_nova_denuncia_post(self):
        app.usuario_logado_id = self.usuario_padrao_id
        data = {
            'titulo': 'Denúncia Teste Automatizado SARA',
            'descricao': 'Descrição detalhada do relato para validação dos 16 testes do sistema SARA.',
            'tipo': 'moral',
            'empresa': 'Tech Test Corp',
            'area_trabalho': 'Tecnologia',
            'cidade': 'Recife',
            'anonima': 'true'
        }
        res = self.client.post('/nova_denuncia', data=data, follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, '/')

        with app.app.app_context():
            den = app.Denuncia.query.filter_by(titulo='Denúncia Teste Automatizado SARA').first()
            self.assertIsNotNone(den)
            self.__class__.denuncia_teste_id = den.id

    def test_07_selecionar_e_ver_denuncia(self):
        den_id = getattr(self.__class__, 'denuncia_teste_id', None)
        if not den_id:
            with app.app.app_context():
                d = app.Denuncia.query.first()
                den_id = d.id

        res_post = self.client.post('/selecionar_denuncia', data={'denuncia_id': str(den_id)}, follow_redirects=False)
        self.assertEqual(res_post.status_code, 302)
        self.assertEqual(res_post.location, '/ver_denuncia')
        self.assertEqual(app.denuncia_atual_id, den_id)

        res_get = self.client.get('/ver_denuncia')
        self.assertEqual(res_get.status_code, 200)
        self.assertIn(b'Apoiar este relato', res_get.data)

    def test_08_comentar_post(self):
        app.usuario_logado_id = self.usuario_padrao_id
        den_id = getattr(self.__class__, 'denuncia_teste_id', None) or app.denuncia_atual_id
        app.denuncia_atual_id = den_id

        data = {
            'texto': 'Comentário de solidariedade enviado pelo teste automatizado.',
            'anonimo': 'true'
        }
        res = self.client.post('/comentar', data=data, follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, '/ver_denuncia')

        with app.app.app_context():
            com = app.Comentario.query.filter_by(texto='Comentário de solidariedade enviado pelo teste automatizado.').first()
            self.assertIsNotNone(com)

    def test_09_apoio_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        den_id = getattr(self.__class__, 'denuncia_teste_id', None) or app.denuncia_atual_id
        app.denuncia_atual_id = den_id

        with app.app.app_context():
            d_before = app.db.session.get(app.Denuncia, den_id)
            apoios_antes = d_before.apoios or 0

        res = self.client.get('/apoio', follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, '/ver_denuncia')

        with app.app.app_context():
            d_after = app.db.session.get(app.Denuncia, den_id)
            self.assertNotEqual(d_after.apoios, None)

    def test_10_perfil_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        res = self.client.get('/perfil')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Suas Den', res.data)
        self.assertIn(b'Mariana Alves', res.data)

    def test_11_selecionar_editar_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        den_id = getattr(self.__class__, 'denuncia_teste_id', None)
        if not den_id:
            with app.app.app_context():
                d = app.Denuncia.query.filter_by(usuario_id=self.usuario_padrao_id).first()
                den_id = d.id

        res_post = self.client.post('/selecionar_editar', data={'denuncia_id': str(den_id)}, follow_redirects=False)
        self.assertEqual(res_post.status_code, 302)
        self.assertEqual(res_post.location, '/editar')
        self.assertEqual(app.denuncia_atual_id, den_id)

        res_get = self.client.get('/editar')
        self.assertEqual(res_get.status_code, 200)
        self.assertIn(b'Editar Den', res_get.data)

    def test_12_editar_post(self):
        app.usuario_logado_id = self.usuario_padrao_id
        den_id = getattr(self.__class__, 'denuncia_teste_id', None) or app.denuncia_atual_id
        app.denuncia_atual_id = den_id

        data = {
            'titulo': 'Denúncia Editada no Teste',
            'descricao': 'Descrição alterada com sucesso durante o teste automatizado.',
            'tipo': 'moral',
            'empresa': 'Tech Test Corp Atualizada',
            'area_trabalho': 'Tecnologia',
            'cidade': 'Campinas',
            'anonima': 'true'
        }
        res = self.client.post('/editar', data=data, follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, '/perfil')

        with app.app.app_context():
            d = app.db.session.get(app.Denuncia, den_id)
            self.assertEqual(d.titulo, 'Denúncia Editada no Teste')
            self.assertEqual(d.empresa, 'Tech Test Corp Atualizada')

    def test_13_minhas_denuncias_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        res = self.client.get('/minhas_denuncias')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Minhas Den', res.data)

    def test_14_filtro_area_get(self):
        res = self.client.get('/area/Tecnologia')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Tecnologia', res.data)

    def test_15_filtro_cidade_get(self):
        res = self.client.get('/filtrar_localizacao?cidade=Recife')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Recife', res.data)

    def test_16_deletar_denuncia_get(self):
        app.usuario_logado_id = self.usuario_padrao_id
        den_id = getattr(self.__class__, 'denuncia_teste_id', None)
        if not den_id:
            with app.app.app_context():
                d = app.Denuncia.query.filter_by(usuario_id=self.usuario_padrao_id).first()
                if d:
                    den_id = d.id

        if den_id:
            res = self.client.get(f'/deletar?id={den_id}', follow_redirects=False)
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, '/perfil')
            with app.app.app_context():
                d_deleted = app.db.session.get(app.Denuncia, den_id)
                self.assertIsNone(d_deleted)


if __name__ == '__main__':
    unittest.main(verbosity=2)
