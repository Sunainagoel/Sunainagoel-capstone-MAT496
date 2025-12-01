import sys
import warnings
warnings.filterwarnings("ignore")
from graph import app
from dotenv import load_dotenv
from data import SAMPLES

load_dotenv()

def get_user_input():
    """Helper to get multi-line input from the user."""
    print("\n(Enter your text. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) on a new line to finish, or just press Enter twice quickly)")
    lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines)

if __name__ == "__main__":
    print("="*40)
    print("   CAREER GAP ANALYZER AGENT")
    print("="*40)
    print("Select an input mode:")
    print("1. Run with Sample Data (Python Dev Scenario)")
    print("2. Run with Sample Data (Data Science Scenario)")
    print("3. Enter Custom Text (Interactive)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    job_desc = ""
    resume_text = ""
    
    if choice == "1":
        print(f"\n--- Loading {SAMPLES[0]['name']} ---")
        job_desc = SAMPLES[0]["jd"]
        resume_text = SAMPLES[0]["resume"]
        
    elif choice == "2":
        print(f"\n--- Loading {SAMPLES[1]['name']} ---")
        job_desc = SAMPLES[1]["jd"]
        resume_text = SAMPLES[1]["resume"]
        
    elif choice == "3":
        print("\n--- Custom Input Mode ---")
        print("\n[1/2] PASTE THE JOB DESCRIPTION BELOW:")
        job_desc = get_user_input()
        
        print("\n[2/2] PASTE THE RESUME BELOW:")
        resume_text = get_user_input()
        
        if len(job_desc) < 10 or len(resume_text) < 10:
            print("\n[Error] Inputs too short. Please try again.")
            sys.exit()
    else:
        print("Invalid selection.")
        sys.exit()

    # Build State
    initial_state = {
        "job_description": job_desc,
        "resume_text": resume_text,
        "learning_plan": [],
    }

    print("\n" + "-"*40)
    print("Starting Agent execution...")
    print("-"*40)
    
    # Run the Graph
    try:
        final_state = app.invoke(initial_state)
        
        print("\n" + "="*30)
        print("FINAL REPORT")
        print("="*30 + "\n")
        print(final_state["final_report"])
        
        if final_state.get("gap_data"):
            print("\n[Debug] Missing Skills Found:", final_state["gap_data"].missing_technical_skills)
            
    except Exception as e:
        print(f"An error occurred during execution: {e}")