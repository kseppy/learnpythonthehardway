dancers = ['Pavlova', 'Osipova', 'Ferri', 'Mearns']
musicians = ['Stern', 'Hahn', 'Heifetz', 'Bell']
tempi = ['Vivace', 1, 'Lento', 2, 'Agitato', 3, 'Allegro', 4]

for dancer in dancers: 
	print(f"A dancer of type: {dancer}")

for musician in musicians:
	print(f"A musician of type: {musician}")

for i in tempi: 
	print(f"I got {i}")

artists = []

for a in range(0, 6):
	print(f"Adding {a} to the list.")
	artists.append(a)

for a in artists:
	print(f"Artist was: {a}")