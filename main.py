import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

movies = pd.read_csv('submodul1/tmdb_movies.csv')
genres = pd.read_csv('submodul1/tmdb_genres.csv')
# ZADANIE 1
q3 = movies['vote_count'].quantile(0.75)
top_movies = movies[movies['vote_count'] > q3].sort_values('vote_average', ascending=False).head(10)

print("10 najlepiej ocenianych filmów z liczbą głosów powyżej 3. kwartyla:")
print()
for _,row in top_movies.iterrows():
    print(row['title'])

# ZADANIE 2

movies['release_year'] = pd.to_datetime(movies['release_date']).dt.year
target_movies = movies[(movies['release_year'] >= 2010) & (movies['release_year'] <=2016)]


def million(x, pos):
        return '{:2.1f}M'.format(x*1e-6)

# Grupowanie po roku i obliczanie średniego budżetu oraz przychodu
srednie = target_movies.groupby('release_year')[['budget', 'revenue']].mean()

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.68,0.8])

axes.set_title('Średni przychód i budżet filmu w latach 2010-2016', pad=20)
axes.set_xlabel('Rok')
axes.set_ylabel('Kwota (w milionach)')

axes.bar(srednie.index, srednie['revenue'], label='revenue')
axes.plot(srednie.index, srednie['budget'], label='budget', color='red')

formatter = plt.FuncFormatter(million)
axes.yaxis.set_major_formatter(formatter)
axes.legend(loc=(1.05,0.90))

#plt.show()

# ZADANIE 3
movies = pd.merge(movies, genres, left_on='genre_id', right_on='Unnamed: 0', how='left')
print(movies[['title', 'genre_id', 'genres']].head(2))
print()

# ZADANIE 4

top_genre = movies['genres'].value_counts().head(1)
print(f"Najczęściej występujący gatunek w bazie filmów: {top_genre.index[0]}")
print(f"Liczba wystąpień: {top_genre.values[0]}")
print()

# ZADANIE 5

top_runtime_genre = movies.groupby('genres')['runtime'].mean().sort_values(ascending=False).head(1)
print(f"Gatunek ze średnim  najdłuższym czasem trwania: {top_runtime_genre.index[0]}")
print(f"Średni czas trwania: {top_runtime_genre.values[0]} min")
print()



# ZADANIE 6
#Stwórz histogram czasu trwania filmów z gatunku, który cechuje się największym średnim czasem trwania.
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])

longest_genre = top_runtime_genre.index[0]
genre_movies = movies[movies['genres'] == longest_genre]

axes.set_title(f'Histogram czasu trwania filmów z gatunku {longest_genre}')
axes.set_xlabel('Czas trwania (minuty)')
axes.set_ylabel('Liczba filmów')

axes.hist(genre_movies['runtime'], bins=15)

plt.show()















