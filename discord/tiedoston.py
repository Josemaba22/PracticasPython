def k():
      nimi = input("Anna tiedoston nimi: ")
      return nimi

def main():
        tiedosto = k()
        try:
            open(tiedosto, "r")
            tiedosto3 = int(tiedosto + 313)
            print("Saatiin tulos ", tiedosto3)
        except IOError:
          print("Virheellinen tiedostonnimi")
        except (TypeError, ValueError):
          print("Tiedoston sisältö virheellinen!")

main()
