import customtkinter as ctk
from tkinter import messagebox
from iqa.iqa_calculator import IQA

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SistemaIQA_Industrial(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IHM - Monitoramento Hídrico v1.0")
        self.geometry("750x650")
        
        # Base de Dados com Notação Química e Parâmetros Ambientais
        self.passos = [
    {
        "id": "8",
        "simbolo": "O₂",
        "nome": "Oxigênio Dissolvido (O₂)",
        "chave": "oxigenio_dissolvido",
        "unidade": "mg/L",
        "desc": "Capacidade de suporte à vida aeróbica no corpo hídrico.",
        "dica": "⚠️ ALERTA DE ANOXIA: Valores abaixo de 2.0 mg/L tornam a vida aquática inviável por asfixia. \nCAUSA: Geralmente associada ao descarte de esgoto orgânico não tratado.",
        "guia": "REFERÊNCIA CONAMA CLASSE 2: Ideal acima de 5.0 mg/L.",
        "cor": "#3b8ed0",
        "min_math": 0.01
    },
    {
        "id": "B1",
        "simbolo": "Co",
        "nome": "Coliformes Termotolerantes",
        "chave": "coliformes_fecais",
        "unidade": "NMP/100mL",
        "desc": "Indicador microbiológico de contaminação por fezes.",
        "dica": "⚠️ RISCO SANITÁRIO: Altas densidades indicam presença de patógenos (vírus/bactérias). \nCAUSA: Falhas no saneamento básico ou escoamento de pastagens.",
        "guia": "REFERÊNCIA BALNEABILIDADE: Ideal abaixo de 1000 NMP/100mL.",
        "cor": "#a67c52",
        "min_math": 0.0
    },
    {
        "id": "1",
        "simbolo": "pH",
        "nome": "Potencial Hidrogeniônico (pH)",
        "chave": "ph",
        "unidade": "0-14",
        "desc": "Mede o equilíbrio entre acidez e alcalinidade da água.",
        "dica": "⚠️ DESEQUILÍBRIO QUÍMICO: Valores extremos aumentam a toxicidade de metais pesados. \nCAUSA: Despejos químicos industriais ou características geológicas locais.",
        "guia": "REFERÊNCIA CETESB: Faixa ideal entre 6.0 e 9.0.",
        "cor": "#2fa572",
        "min_math": 0.1
    },
    {
        "id": "B2",
        "simbolo": "DBO",
        "nome": "Demanda Bioquímica (DBO)",
        "chave": "dbo",
        "unidade": "mg/L",
        "desc": "Mede o consumo de oxigênio por microrganismos.",
        "dica": "⚠️ SOBRECARGA ORGÂNICA: Quanto maior a DBO, mais oxigênio é roubado da fauna. \nCAUSA: Presença excessiva de matéria orgânica em decomposição.",
        "guia": "REFERÊNCIA PARA ÁGUAS LIMPAS: Ideal abaixo de 5.0 mg/L.",
        "cor": "#c33c3c",
        "min_math": 0.1
    },
    {
        "id": "7",
        "simbolo": "N",
        "nome": "Nitrogênio Total (N)",
        "chave": "nitrogenio_total",
        "unidade": "mg/L",
        "desc": "Nutriente essencial, mas perigoso em excesso.",
        "dica": "⚠️ EUTROFIZAÇÃO: Nutre algas que bloqueiam a luz solar e matam o rio. \nCAUSA: Fertilizantes agrícolas e detergentes domésticos.",
        "guia": "REFERÊNCIA DE PREVENÇÃO: Ideal abaixo de 1.0 mg/L.",
        "cor": "#8d6e63",
        "min_math": 0.01
    },
    {
        "id": "15",
        "simbolo": "P",
        "nome": "Fósforo Total (P)",
        "chave": "fosforo_total",
        "unidade": "mg/L",
        "desc": "Principal gatilho para o florescimento de algas.",
        "dica": "⚠️ FLORESCIMENTO TÓXICO: Estimula algas que podem liberar toxinas na água. \nCAUSA: Efluentes industriais e lavagem de solos adubados.",
        "guia": "REFERÊNCIA AMBIENTAL: Ideal abaixo de 0.02 mg/L.",
        "cor": "#ffb74d",
        "min_math": 0.01
    },
    {
        "id": "F1",
        "simbolo": "UT",
        "nome": "Turbidez (UNT)",
        "chave": "turbidez",
        "unidade": "UNT",
        "desc": "Mede a claridade da água e presença de partículas.",
        "dica": "⚠️ BLOQUEIO FÓTICO: Impede a fotossíntese de plantas no fundo do rio. \nCAUSA: Erosão de margens, desmatamento ou mineração.",
        "guia": "REFERÊNCIA DE POTABILIDADE: Ideal abaixo de 1.0 UNT.",
        "cor": "#78909c",
        "min_math": 0.01
    },
    {
        "id": "F2",
        "simbolo": "ST",
        "nome": "Sólidos Totais (ST)",
        "chave": "solidos_totais",
        "unidade": "mg/L",
        "desc": "Massa total de materiais dissolvidos e suspensos.",
        "dica": "⚠️ ASSOREAMENTO: Excesso de sólidos pode 'entupir' o leito do rio. \nCAUSA: Esgotos e arraste de terra por falta de mata ciliar.",
        "guia": "REFERÊNCIA CETESB: Ideal abaixo de 500 mg/L.",
        "cor": "#546e7a",
        "min_math": 0.1
    },
    {
        "id": "0",
        "simbolo": "Alt",
        "nome": "Altitude Local (m)",
        "chave": "altitude",
        "unidade": "Metros",
        "desc": "Altura do ponto de coleta em relação ao mar.",
        "dica": "ℹ️ CORREÇÃO FÍSICA: A altitude altera a pressão onde o oxigênio se dissolve. \nNOTA: É um dado geográfico fixo do local da coleta.",
        "guia": "DADO DE ENTRADA: Ex: São Paulo (760m), Litoral (0m).",
        "cor": "#9e9e9e",
        "min_math": 0.0
    },
    {
        "id": "0",
        "simbolo": "T",
        "nome": "Temperatura (ºC)",
        "chave": "temperatura",
        "unidade": "Graus Celsius",
        "desc": "Mede a energia térmica do corpo d'água.",
        "dica": "ℹ️ DINÂMICA TÉRMICA: Águas quentes retêm menos oxigênio que águas frias. \nCAUSA: Exposição solar ou despejos de águas de resfriamento industrial.",
        "guia": "REFERÊNCIA TROPICAL: Geralmente entre 15ºC e 35ºC.",
        "cor": "#ff5722",
        "min_math": 0.1
    }
]
        
        self.valores_coletados = {}
        self.passo_atual = 0

        self.barra_progresso = ctk.CTkProgressBar(self, width=550, height=12)
        self.barra_progresso.pack(pady=25)
        self.barra_progresso.set(0)

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both", padx=50)

        self.exibir_passo()

    def exibir_passo(self):
        for widget in self.container.winfo_children(): widget.destroy()
        p = self.passos[self.passo_atual]

        # Cabeçalho Técnico
        ctk.CTkLabel(self.container, text=f"MONITORAMENTO TÉCNICO AMBIENTAL - FASE {self.passo_atual + 1}/10", font=("Arial", 11, "bold"), text_color="#777777").pack()
        
        # Nome e Símbolo (Simulando Tabela Periódica/Notação)
        titulo_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        titulo_frame.pack(pady=10)
        
        ctk.CTkLabel(titulo_frame, text=p["simbolo"], font=("Arial", 32, "bold"), text_color=p["cor"]).pack(side="left", padx=15)
        ctk.CTkLabel(titulo_frame, text=p["nome"], font=("Arial", 26, "bold")).pack(side="left")

	# 2. QUADRADO DA TABELA PERIÓDICA (O ícone novo)
        periodic_frame = ctk.CTkFrame(self.container, width=120, height=120, border_width=3, border_color=p["cor"], fg_color="#1a1a1a")
        periodic_frame.pack(pady=10)
        periodic_frame.pack_propagate(False)

        ctk.CTkLabel(periodic_frame, text=p["id"], font=("Arial", 14, "bold"), text_color=p["cor"]).place(x=10, y=5)
        ctk.CTkLabel(periodic_frame, text=p["simbolo"], font=("Arial", 40, "bold"), text_color=p["cor"]).place(relx=0.5, rely=0.5, anchor="center")
        
        # Box de Informação Didática Profissional
        info_box = ctk.CTkFrame(self.container, fg_color="#1e1e1e", border_width=1, border_color=p["cor"], corner_radius=12)
        info_box.pack(pady=15, fill="x")
        ctk.CTkLabel(info_box, text=p["desc"], font=("Arial", 14, "bold")).pack(pady=8)
        ctk.CTkLabel(info_box, text=p["dica"], font=("Arial", 12, "italic"), text_color="#ffcc00", wraplength=550).pack(pady=8)

        # Entrada de Dados
        self.entrada_var = ctk.CTkEntry(self.container, placeholder_text=f"Inserir valor ({p['unidade']})", 
                                        width=320, height=65, font=("Arial", 26), justify="center", border_color=p["cor"])
        self.entrada_var.pack(pady=25)
        self.entrada_var.focus()

        ctk.CTkLabel(self.container, text=f"PARÂMETRO DE REFERÊNCIA (CONAMA/CETESB):\n{p['guia']}", font=("Arial", 12)).pack(pady=10)

        # Navegação
        btn_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        btn_frame.pack(pady=30)

        if self.passo_atual > 0:
            ctk.CTkButton(btn_frame, text="RETROCEDER", fg_color="#444444", hover_color="#333333", width=140, command=self.voltar).pack(side="left", padx=10)

        btn_text = "AVANÇAR" if self.passo_atual < 9 else "GERAR DIAGNÓSTICO"
        ctk.CTkButton(btn_frame, text=btn_text, width=220, height=50, command=self.proximo, font=("Arial", 15, "bold")).pack(side="left", padx=10)

    def proximo(self):
        try:
            val_text = self.entrada_var.get().strip().replace(',', '.')
            if not val_text: return
            
            valor = float(val_text)
            p_info = self.passos[self.passo_atual]

            # TRAVA ANTI-ERRO (Poka-Yoke)
            if valor < 0:
                messagebox.showerror("Erro de Domínio", "Valores negativos não são aplicáveis a este parâmetro físico-químico.")
                return
            
            # Ajuste de segurança para o motor de cálculo
            if valor == 0 and p_info["min_math"] > 0:
                valor = p_info["min_math"]

            self.valores_coletados[p_info["chave"]] = valor
            
            if self.passo_atual < 9:
                self.passo_atual += 1
                self.barra_progresso.set(self.passo_atual / 9)
                self.exibir_passo()
            else:
                self.executar_calculo_final()
        except ValueError:
            messagebox.showwarning("Erro de Sintaxe", "Por favor, utilize apenas algarismos numéricos.")

    def voltar(self):
        self.passo_atual -= 1
        self.barra_progresso.set(self.passo_atual / 9)
        self.exibir_passo()

    def executar_calculo_final(self):
        for widget in self.container.winfo_children(): widget.destroy()
        try:
            # O motor de cálculo IQA agora recebe os 10 parâmetros (incluindo altitude e temperatura)
            res = IQA(**self.valores_coletados)
            
            # Tratamento de precisão real/complexa
            iqa_num = res['iqa'].real if hasattr(res['iqa'], 'real') else res['iqa']
            iqa_num = round(float(iqa_num), 2)
            
            qualidade = res['qualidade']
            cor = "#2fa572" if qualidade in ["Boa", "Ótima"] else "#c33c3c"
            if qualidade == "Regular": cor = "#c39b3c"

            ctk.CTkLabel(self.container, text="LAUDO TÉCNICO DE QUALIDADE HÍDRICA", font=("Arial", 24, "bold")).pack(pady=40)
            
            res_box = ctk.CTkFrame(self.container, border_width=3, border_color=cor, fg_color="#1a1a1a", corner_radius=20)
            res_box.pack(pady=10, padx=30, fill="x")

            ctk.CTkLabel(res_box, text=f"IQA FINAL: {iqa_num}", font=("Arial", 52, "bold"), text_color=cor).pack(pady=20)
            ctk.CTkLabel(res_box, text=f"STATUS: {qualidade.upper()}", font=("Arial", 22, "bold")).pack(pady=15)

            ctk.CTkButton(self.container, text="INICIAR NOVA ANÁLISE", command=self.resetar, width=300, height=55, font=("Arial", 16, "bold")).pack(pady=50)
        except Exception as e:
            messagebox.showerror("Erro de Processamento", f"O motor de cálculo falhou ao processar a amostra: {e}")
            self.resetar()

    def resetar(self):
        self.passo_atual = 0; self.valores_coletados = {}; self.barra_progresso.set(0); self.exibir_passo()

if __name__ == "__main__":
    app = SistemaIQA_Industrial()
    app.mainloop()