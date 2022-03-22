from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from comunidadeimpressionadora.models import User
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = User.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro E-mail ou faça login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionadoras')
    curso_sql = BooleanField('SQL Impresioandor')
    botao_submit_editarperfil = SubmitField('Comfiramar mudanças')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = User.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail, cadastre outro e-mail.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui.', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')