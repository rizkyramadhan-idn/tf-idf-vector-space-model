#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TF-IDF

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10, sqrt
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# In[27]:


# Mendapatkan list dari seluruh kata-kata yang ada pada list dokumen
# di mana kata-kata tersebut bukan stopwords dan sudah di-stemming.

def get_list_of_word(list_of_dokumen, stopwords):
    list_of_word = []

    for sentence in list_of_dokumen:
        for word in sentence.split(" "):
            stemmed_word = stemmer.stem(word)
            if word not in stopwords and stemmed_word not in list_of_word:
                list_of_word.append(stemmed_word)

    return list_of_word


# In[32]:


# Membuat sebuah list yang berisi kumpulan
# word yang nilai awalnya adalah 0

def create_term_frequency(list_of_word, length_dokumen_with_kk):
    term_frequency = []

    for _ in range(length_dokumen_with_kk):
        term_frequency.append(
            dict(zip(list_of_word, [0 for _ in range(len(list_of_word))])))

    return term_frequency


# In[33]:


# Membuat sebuah dictionary yang berisi
# kata-kata untuk term frequency dengan
# nilai awal 0.

def create_document_frequency(list_of_word):
    return dict(zip(list_of_word, [0 for _ in range(len(list_of_word))]))


# In[34]:


# Mendapatkan d_df. Di mana itu adalah pembagian
# antara jumlah dokumen dan nilai dokumen frequency.

def get_d_df(length_of_dokumen, document_frequency):
    d_df = {}

    for key, value in document_frequency.items():
        d_df[key] = length_of_dokumen / value

    return d_df


# In[35]:


# Mendapatkan nilai idf dari d_df.

def get_idf(d_df):
    idf = {}

    for key, value in d_df.items():
        idf[key] = round(log10(value), 3)

    return idf


# In[37]:


# Mendapatkan W_q_t. Di mana itu merupakan perkalian antara tf * idf.

def get_w_q_t(term_frequency, idf):
    w_q_t = []

    for index, document in enumerate(term_frequency):
        w_q_t.append({})
        for key, value in document.items():
            w_q_t[index][key] = value * idf[key]

    return w_q_t


# In[38]:


# Mengembalikan list yang berisi bobot dari
# kata kunci di setiap dokumen.

def get_bobot_kata_kunci(w_q_t, kata_kunci):
    bobot_kata_kunci = []

    for index, document in enumerate(w_q_t):
        if index > 0:
            bobot_kata_kunci.append({})
            for word in stemmer.stem(kata_kunci).split(" "):
                bobot_kata_kunci[index-1][word] = document[word]

    return bobot_kata_kunci


# In[39]:


# Mendapatkan bobot dari setiap dokumen

def get_bobot_dokumen(list_bobot_kata_kunci):
    bobot_dokumen = []

    for index, dokumen in enumerate(list_bobot_kata_kunci):
        total = 0

        for _, value in dokumen.items():
            total += value

        bobot_dokumen.append({f"bobot_dokumen_{index + 1}": total})

    return bobot_dokumen


# In[40]:


# Mendapatkan q_d. Di mana q_d merupakan W_q_t kuadrat.
# Hasil totalnya merupakan penjumlahan dari seluruh
# nilanya dan diakarkan.

def get_q_d(w_q_t):
    q_d = []

    for index, dokumen in enumerate(w_q_t):
        q_d.append({})
        total = 0
        for key, value in dokumen.items():
            q_d[index][key] = round(value ** 2, 3)
            total += q_d[index][key]
        q_d[index]["total_akar"] = round(sqrt(total), 3)

    return q_d


# In[5]:


factory = StemmerFactory()

stemmer = factory.create_stemmer()
stopwords_factory = StopWordRemoverFactory()


# In[4]:


stopwords = stopwords_factory.get_stop_words()


# In[6]:


stopwords


# In[7]:


# Kata kunci

kata_kunci = "pengetahuan logistik"

# Dokumen

dokumen_1 = "manajemen transaksi logistik"
dokumen_2 = "pengetahuan antar individu"
dokumen_3 = "dalam manajemen pengetahuan terdapat transfer pengetahuan logistik"


# In[8]:


# List yang berisi kumpulan dokumen dan
# ukuran dari list tersebut.

list_of_dokumen = [dokumen_1, dokumen_2, dokumen_3]
length_of_dokumen = len(list_of_dokumen)
length_of_dokumen_with_kk = len([kata_kunci, dokumen_1, dokumen_2, dokumen_3])


# In[19]:


list_of_dokumen


# In[30]:


# Berisi kata-kata yang berasal dari list dokumen.

list_of_word = get_list_of_word(list_of_dokumen, stopwords)


# In[31]:


list_of_word


# In[41]:


term_frequency = create_term_frequency(list_of_word, length_of_dokumen_with_kk)


# In[42]:


term_frequency


# In[43]:


# Menambahkan nilai dari term frequency sesuai
# dengan kemunculan setiap kata pada dokumen.

for index, sentence in enumerate([kata_kunci, dokumen_1, dokumen_2, dokumen_3]):
    for word in stemmer.stem(sentence).split(" "):
        if word in term_frequency[index]:
            term_frequency[index][word] += 1


# In[44]:


term_frequency


# In[49]:


document_frequency = create_document_frequency(list_of_word)


# In[50]:


document_frequency


# In[51]:


# Menambahkan nilai untuk document frequency
# dengan cara menambahkan kemunculan pada
# setiap dokumen.

for index, sentence in enumerate(term_frequency):
    if index > 0:
        for key, value in sentence.items():
            if value:
                document_frequency[key] += 1


# In[52]:


document_frequency


# In[53]:


d_df = get_d_df(length_of_dokumen, document_frequency)


# In[54]:


d_df


# In[55]:


idf = get_idf(d_df)


# In[56]:


idf


# In[57]:


w_q_t = get_w_q_t(term_frequency, idf)


# In[58]:


w_q_t


# In[59]:


bobot_kata_kunci = get_bobot_kata_kunci(w_q_t, kata_kunci)


# In[60]:


bobot_kata_kunci


# In[61]:


list_bobot_dokumen = get_bobot_dokumen(bobot_kata_kunci)


# In[62]:


list_bobot_dokumen


# In[63]:


q_d = get_q_d(w_q_t)


# In[64]:


q_d


# In[65]:


bobot_kata_kunci_q_d = {}


# In[66]:


bobot_kk_dan_dokumen = {}


# In[67]:


sum_of_tf_q_d = []


# In[68]:


bobot_sum_of_tf_q_d = {}


# In[69]:


for word in stemmer.stem(kata_kunci).split(" "):
    bobot_kata_kunci_q_d[word] = q_d[0][word]


# In[70]:


for index, dokumen in enumerate(q_d):
    for key, value in dokumen.items():
        if key == "total_akar":
            if index == 0:
                bobot_kk_dan_dokumen["total_bobot_kk"] = value
            else:
                bobot_kk_dan_dokumen[f"total_bobot_dokumen_{index}"] = value


# In[71]:


for index, dokumen in enumerate(term_frequency):
    if index > 0:
        sum_of_tf_q_d.append({})
        for key, value in dokumen.items():
            if key in bobot_kata_kunci_q_d:
                sum_of_tf_q_d[index-1][key] = value * bobot_kata_kunci_q_d[key]


# In[72]:


for index, dokumen in enumerate(sum_of_tf_q_d):
    bobot_sum_of_tf_q_d[f"bobot_sum_tf_q_d_{index+1}"] = 0
    for key, value in dokumen.items():
        bobot_sum_of_tf_q_d[f"bobot_sum_tf_q_d_{index+1}"] += value


# In[73]:


bobot_sum_tf_q_d_1 = bobot_sum_of_tf_q_d["bobot_sum_tf_q_d_1"]
bobot_sum_tf_q_d_2 = bobot_sum_of_tf_q_d["bobot_sum_tf_q_d_2"]
bobot_sum_tf_q_d_3 = bobot_sum_of_tf_q_d["bobot_sum_tf_q_d_3"]


# In[74]:


total_bobot_kk = bobot_kk_dan_dokumen["total_bobot_kk"]
total_bobot_dokumen_1 = bobot_kk_dan_dokumen["total_bobot_dokumen_1"]
total_bobot_dokumen_2 = bobot_kk_dan_dokumen["total_bobot_dokumen_2"]
total_bobot_dokumen_3 = bobot_kk_dan_dokumen["total_bobot_dokumen_3"]


# In[75]:


hasil_bobot_dokumen_1 = round(sqrt(bobot_sum_tf_q_d_1) /
                              (total_bobot_kk / total_bobot_dokumen_1), 3)
hasil_bobot_dokumen_2 = round(sqrt(bobot_sum_tf_q_d_2) /
                              (total_bobot_kk / total_bobot_dokumen_2), 3)
hasil_bobot_dokumen_3 = round(sqrt(bobot_sum_tf_q_d_3) /
                              (total_bobot_kk / total_bobot_dokumen_3), 3)


# In[76]:


print("\nBobot q/d: \n")

print(bobot_sum_tf_q_d_1)
print(bobot_sum_tf_q_d_2)
print(bobot_sum_tf_q_d_3)


# In[77]:


print("\nBobot tf * Wq: \n")

print(total_bobot_kk)
print(total_bobot_dokumen_1)
print(total_bobot_dokumen_2)
print(total_bobot_dokumen_3)


# In[78]:


print("\nHasil akhir: \n")

print(hasil_bobot_dokumen_1)
print(hasil_bobot_dokumen_2)
print(hasil_bobot_dokumen_3)


# In[95]:


hasil_akhir = [
    {"nama": "Dokumen 1", "nilai": hasil_bobot_dokumen_1},
    {"nama": "Dokumen 2", "nilai": hasil_bobot_dokumen_2},
    {"nama": "Dokumen 3", "nilai": hasil_bobot_dokumen_3},
]


# In[96]:


hasil_akhir


# In[97]:


hasil_akhir.sort(key=lambda item: item.get("nilai"), reverse=True)


# In[98]:


hasil_akhir


# In[ ]:




