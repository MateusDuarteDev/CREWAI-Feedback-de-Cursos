
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
import random

# Dados de feedback
feedbacks_positivos = 16
feedbacks_negativos = 9

# Palavras-chave positivas e negativas
palavras_chave_positivas = ["excelente", "bem organizado", "fácil entendimento", "relevante", "prático", "envolvente", "claro", "detalhado", "eficaz", "enriquecedor", "satisfatório"]
palavras_chave_negativas = ["frustrado", "falta de interação", "problemas técnicos", "dificuldades de acesso", "falta de clareza", "superficial", "básico", "curto", "insatisfação", "não atendeu às expectativas"]


# --- Gráfico de Pizza ---
labels = 'Positivos', 'Negativos'
sizes = [feedbacks_positivos, feedbacks_negativos]
colors = ['green', 'red']
explode = (0.1, 0)  # explode 1st slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Porcentagem de Feedbacks Positivos e Negativos')
plt.savefig('grafico_pizza.png')


# --- Gráfico de Barras ---
labels = ['Positivos', 'Negativos']
values = [feedbacks_positivos, feedbacks_negativos]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['green', 'red'])
plt.title('Número de Feedbacks Positivos e Negativos')
plt.ylabel('Número de Feedbacks')
plt.savefig('grafico_barras.png')


# --- Nuvem de Palavras (Positivas) ---
stopwords = set(STOPWORDS)
stopwords.update(["o", "a", "e", "da", "de", "em", "um", "uma", "para", "com", "que", "os", "as", "do", "no", "na", "ao", "aos", "nas", "se", "são", "é", "seu", "sua", "seus", "suas"])

text_positivo = " ".join(palavras_chave_positivas)
wordcloud_positivo = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords, colormap='Greens').generate(text_positivo)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_positivo, interpolation='bilinear')
plt.axis("off")
plt.title('Nuvem de Palavras - Feedbacks Positivos')
plt.savefig('nuvem_palavras_positivas.png')


# --- Nuvem de Palavras (Negativas) ---
text_negativo = " ".join(palavras_chave_negativas)
wordcloud_negativo = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords, colormap='Reds').generate(text_negativo)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_negativo, interpolation='bilinear')
plt.axis("off")
plt.title('Nuvem de Palavras - Feedbacks Negativos')
plt.savefig('nuvem_palavras_negativas.png')

plt.show()
