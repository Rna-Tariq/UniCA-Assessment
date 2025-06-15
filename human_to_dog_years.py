def human_to_dog_years(human_years):
    if human_years <= 0:
        print("Error: Age cannot be negative nor zero.")
        return None
    elif human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + (human_years - 2) * 4
    return dog_years

def main():
    while True:
        try:
            human_years = input("Enter the dog's age in human years: ")
            if human_years.lower() in ['quit', 'q', 'exit']:
                print("Goodbye!")
                break
            else:
                human_years = float(human_years)
                dog_years = human_to_dog_years(human_years)
                
                if dog_years is not None:
                    print(f"{human_years} human years = {dog_years:.1f} dog years\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except ValueError:
            print("Please enter a valid number or type 'quit' to exit.\n")

if __name__ == "__main__":
    main()
