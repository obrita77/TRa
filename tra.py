# Importação das bibliotecas do Kivy necessárias para criar o app
from kivy.app import App                  # Classe base para criar o aplicativo
from kivy.uix.boxlayout import BoxLayout  # Layout para organizar widgets em caixas
from kivy.uix.label import Label          # Widget para exibir textos
from kivy.uix.button import Button        # Botões clicáveis
from kivy.uix.textinput import TextInput  # Campo de entrada de texto
from kivy.uix.scrollview import ScrollView # Permite rolagem na tela
from kivy.uix.gridlayout import GridLayout # Layout em grade para exibir as tarefas

# Classe principal que define a interface do aplicativo
class ListaTarefas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Chama o construtor da classe pai (BoxLayout)

        # Define a orientação do layout principal como vertical (empilha os widgets)
        self.orientation = "vertical"
        self.padding = 20   # Define um espaçamento interno de 20px nas bordas
        self.spacing = 15   # Define um espaço de 15px entre os widgets

        # -----------------------------
        # CRIAÇÃO DO TÍTULO DO APLICATIVO
        # -----------------------------
        self.titulo = Label(
            text="[b][color=0080ff]MINHA LISTA DE ATIVIDADE[/color][/b]",  # Texto do título com cor azul e negrito
            markup=True,      # Permite usar tags de formatação no texto
            font_size=26,     # Tamanho da fonte
            size_hint=(1, None),  # Ocupa 100% da largura, mas altura fixa
            height=50         # Altura do título
        )
        self.add_widget(self.titulo)  # Adiciona o título ao layout principal

        # -----------------------------
        # LAYOUT PARA ENTRADA DE TEXTO + BOTÃO ADICIONAR
        # -----------------------------
        entrada_layout = BoxLayout(
            orientation="horizontal",  # Widgets lado a lado
            size_hint=(1, None),       # Ocupa 100% da largura, altura fixa
            height=45,                 # Altura do layout
            spacing=10                 # Espaço de 10px entre os widgets
        )

        # Campo para digitar a tarefa
        self.entrada_tarefa = TextInput(
            hint_text="Digite uma nova tarefa...",  # Texto de placeholder
            multiline=False,    # Permite apenas uma linha de texto
            size_hint=(0.7, 1)  # Ocupa 70% da largura disponível
        )
        entrada_layout.add_widget(self.entrada_tarefa)  # Adiciona o campo ao layout

        # Botão para adicionar tarefa à lista
        self.botao_adicionar = Button(
            text="ADICIONAR",            # Texto do botão
            size_hint=(0.3, 1),          # Ocupa 30% da largura disponível
            background_color=(0, 0.5, 1, 1)  # Cor azul (RGBA)
        )
        # Associa a função "adicionar_tarefa" ao clique do botão
        self.botao_adicionar.bind(on_press=self.adicionar_tarefa)
        entrada_layout.add_widget(self.botao_adicionar)  # Adiciona o botão ao layout

        # Adiciona o layout de entrada ao layout principal
        self.add_widget(entrada_layout)

        # -----------------------------
        # BOTÃO PARA LIMPAR TODAS AS TAREFAS
        # -----------------------------
        self.botao_limpar = Button(
            text="Limpar Lista",       # Texto do botão
            size_hint=(1, None),       # Ocupa toda a largura
            height=45,                 # Altura fixa
            background_color=(1, 0, 0, 1)  # Cor vermelha (RGBA)
        )
        # Associa a função "limpar_lista" ao clique do botão
        self.botao_limpar.bind(on_press=self.limpar_lista)
        self.add_widget(self.botao_limpar)  # Adiciona o botão ao layout principal

        # -----------------------------
        # ÁREA DE EXIBIÇÃO DAS TAREFAS (COM ROLAGEM)
        # -----------------------------
        scroll = ScrollView(size_hint=(1, 1))  # Área rolável para as tarefas

        # Layout interno para exibir a lista de tarefas em colunas
        self.lista_tarefas_layout = GridLayout(
            cols=1,            # Apenas uma coluna
            spacing=10,        # Espaço de 10px entre as tarefas
            size_hint_y=None   # Altura variável, definida dinamicamente
        )
        # Ajusta a altura do GridLayout de acordo com o número de tarefas
        self.lista_tarefas_layout.bind(minimum_height=self.lista_tarefas_layout.setter("height"))

        # Adiciona o GridLayout dentro do ScrollView
        scroll.add_widget(self.lista_tarefas_layout)

        # Adiciona o ScrollView ao layout principal
        self.add_widget(scroll)

    # -----------------------------
    # FUNÇÃO PARA ADICIONAR UMA NOVA TAREFA
    # -----------------------------
    def adicionar_tarefa(self, instance):
        # Obtém o texto digitado no campo e remove espaços extras
        tarefa_texto = self.entrada_tarefa.text.strip()

        # Se o campo não estiver vazio
        if tarefa_texto:
            # Cria um label para exibir a tarefa na lista
            tarefa = Label(
                text=f"• {tarefa_texto}",  # Texto com marcador
                font_size=18,             # Tamanho do texto
                size_hint_y=None,         # Altura fixa
                height=35,                # Altura do item da lista
                halign="left",            # Alinha o texto à esquerda
                valign="middle"           # Alinha o texto ao centro vertical
            )
            # Permite que o texto quebre de linha automaticamente se for longo
            tarefa.bind(size=tarefa.setter('text_size'))

            # Adiciona o item à lista de tarefas
            self.lista_tarefas_layout.add_widget(tarefa)

            # Limpa o campo de texto após adicionar a tarefa
            self.entrada_tarefa.text = ""
        else:
            # Caso o usuário clique no botão sem digitar nada
            self.entrada_tarefa.hint_text = "⚠ Insira uma tarefa válida!"

    # -----------------------------
    # FUNÇÃO PARA LIMPAR TODAS AS TAREFAS
    # -----------------------------
    def limpar_lista(self, instance):
        # Remove todos os widgets da lista de tarefas
        self.lista_tarefas_layout.clear_widgets()


# Classe principal do aplicativo
class ListaTarefasApp(App):
    def build(self):
        return ListaTarefas()  # Retorna a interface principal


# Ponto de entrada do programa
if __name__ == "__main__":
    ListaTarefasApp().run()  # Executa o aplicativo
