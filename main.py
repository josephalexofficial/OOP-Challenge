from pet import Pet

def main():
    # Create a pet
    my_pet = Pet("Buddy")
    
    # Test the methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
