# 🧠 Análise Inteligente de Feedback de Curso com CREWAI

Este projeto utiliza **Sistema Multiagentes inteligentes com CREWAI** para realizar a **análise automatizada de feedbacks**. O objetivo é identificar pontos fortes e áreas de melhoria de um curso (ou produto), fornecendo gráficos, nuvens de palavras e relatório final detalhado.

---

## ⚙️ Tecnologias Utilizadas

- 🧠 [CREWAI](https://github.com/joaomdmoura/crewAI) — Framework de agentes de IA colaborativos
- 🐍 Python — Linguagem utilizada
- 🧪 LangChain / Gemini — LLMs utilizadas para interpretar e gerar análises
- 🐋 Docker Desktop — Container Virtual

---

## 📌 Funcionalidades

- 🤖 **Análise automática via agentes CREWAI**:
  - Análise dos feedbacks dos clientes.
  - Classificação dos feedbacks em positivos e negativos.
  - Identificação dos motivos que levaram ao feedback do cliente.
  - Recomendação de pontos a melhorar e pontos fortes a se manter.

- 📊 **Geração de relatório final**
O resultado final da execução desse programa é a criação de gráficos e nuvens de palavras para visualização do resultado da análise, juntamente com um relatório final detalhado sobre os feedbacks coletados. Por se tratar de um programa com utilização de LLM, os textos gerados vão ser diferentes a cada execução, sem mudar o resultado final. Alguns detalhes:
  - Gráficos: Geração de 2 gráficos que mostram a quantidade de feedbacks positivos e negativos (Gráfico de Barras e Gráfico de Pizza).
  - Nuvens de Palavras: Geração de 2 nuvens de palavras (positiva e negativa) contendo as principais keywords para classificaçao do feedback.
  - Relatório : Geração em Markdown de um relatório final evidenciando os principais pontos fortes e fracos dos feedbacks, separados por classificação e detalhes. 

---

## 📚 Exemplos de Uso
- Um professor ministra um curso para vários alunos.
- Ao final do curso, o aluno faz a avaliação anônima.
- Os agentes de IA analisam os feedbacks e geram um relatório detalhado dos pontos positivos e negativos:

*"A clareza, organização e relevância do conteúdo foram amplamente elogiadas.  A facilidade de entendimento e a aplicabilidade prática do conhecimento adquirido foram pontos cruciais de satisfação. A presença de exemplos práticos também contribuiu significativamente para a experiência positiva. (Feedbacks 1, 3, 6, 9, 10, 11, 13, 14, 16, 19, 21, 25)"*

*"A superficialidade do conteúdo, a falta de temas esperados e a duração curta do curso foram críticas frequentes.  A falta de clareza em alguns exemplos e a falta de materiais complementares também foram mencionados. (Feedbacks 15, 20, 22, 23, 24)"*

---

## 🧠 Sobre o CREWAI
CREWAI é uma biblioteca para orquestração de múltiplos agentes de inteligência artificial trabalhando de forma colaborativa, ideal para fluxos complexos e análises com múltiplas etapas.

---

## Informações sobre o uso e melhorias futuras :

O agente de IA que gera os gráficos precisa utilizar o **🐋 Docker Desktop** para criar e testar o código em containers virtuais e essa etapa ainda terá melhorias. Portanto, após rodar o programa, o código gerado virá com *''' bash* no início e no fim do código. Basta apagar a primeira e a última linha, rodar o código em sua máquina e os gráficos serão gerados.

---

## 📬 Contato
Desenvolvido por Mateus Duarte e [Adriano Motta](https://github.com/AdrianoCeub)
- 🔗 [LinkedIn](https://www.linkedin.com/in/mateus-duarte-cavalcante/)
- 📧 mateus.dc@hotmail.com

---

⭐ Se você gostou da ideia, contribua com uma estrela!