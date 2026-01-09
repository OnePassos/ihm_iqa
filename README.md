💧 IHM - Monitoramento Hídrico (IQA CETESB)
Esta é uma Interface Homem-Máquina (IHM) industrial desenvolvida para automatizar o cálculo do Índice de Qualidade da Água (IQA), baseada na metodologia da CETESB e nas resoluções do CONAMA. O sistema permite a entrada de dados físico-químicos e retorna diagnósticos precisos sobre a saúde hídrica de mananciais.

Instalação e Configuração
Para registrar o projeto corretamente no seu ambiente Python e visualizar os metadados do autor:

Clone o repositório:
git clone https://github.com/OnePassos/ihm-iqa.git
cd ihm-iqa

Instale o pacote localmente usando o Bash/cmd:

pip install .

Verifique a autoria e versão:

pip show ihm_iqa (Isso confirmará o registro)

Como Utilizar: 

Execute o arquivo principal para abrir a interface gráfica:

python ihm_iqa.py

Funcionalidades Implementadas:

Entrada Assistida: Campos validados para os 9 parâmetros fundamentais.
Correção Termodinâmica: Integração de Altitude e Temperatura para o cálculo exato da saturação de oxigênio.

Poka-Yoke Informativo: Alertas automáticos baseados na CONAMA Classe 2, explicando fenômenos como Eutrofização e Anoxia.

Saída Multiformato: Retorno do valor numérico do IQA e sua classificação qualitativa (Ótima, Boa, Regular, Ruim ou Péssima).


🛠️ Tecnologias Utilizadas
Linguagem: Python 3.
GUI: CustomTkinter (Interface Moderna/Dark Mode).

Motor de Cálculo: Baseado no pacote iqa_calculator.

Gerenciamento: Setuptools para distribuição de pacotes.
