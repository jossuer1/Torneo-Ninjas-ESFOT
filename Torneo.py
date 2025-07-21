def torneo(ninjas):
  while len(ninjas) > 1:
    n1 = ninjas.pop(0)
    n2 = ninjas.pop(0)
    print(f"{n1} VS {n2}")
    ganador = n1
    print(f"Gana{ganador}")
    ninjas.append(ganador)
  print(f"El ganador y finalista es: {ninjas[0]}")

terneo(ninjas)


  

