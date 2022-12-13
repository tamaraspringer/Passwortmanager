
import sys
sys.path.append('./controller')
from controller import Controller
  
        
def main():
    passwordmanaager = Controller()
    passwordmanaager.run()
if __name__ == "__main__":
    main()
    
