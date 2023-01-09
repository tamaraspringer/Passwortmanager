
import sys
sys.path.append('./controller')
from controller import Controller
  
        
def main():
    passwordmanager = Controller()
    passwordmanager.run()
if __name__ == "__main__":
    main()
    
