import gensim

vectors = gensim.models.KeyedVectors.load("/root/app/chive-1.2-mc90.txt")

print(vectors.most_similar("春", topn=10))