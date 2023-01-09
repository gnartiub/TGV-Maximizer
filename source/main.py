
import dotenv
from view.start_view import StartView

# This script is the entry point of your application

dotenv.load_dotenv()
if __name__ == '__main__':
    # run the StartView
    current_view = StartView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()
        
        
        