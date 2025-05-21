import subprocess
import sys

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stderr.strip())
        else:
            print(result.stdout.strip())
    except Exception as e:
        print(f"Command failed: {e}")

def list_vms():
    print("\n--- Active VMs ---")
    run_command("virsh list")

    print("\n--- Inactive VMs ---")
    run_command("virsh list --all")

def start_vm(name):
    run_command(f"virsh start {name}")

def stop_vm(name):
    run_command(f"virsh shutdown {name}")

def get_status(name):
    run_command(f"virsh domstate {name}")

def create_vm(xml_path):
    run_command(f"virsh define {xml_path}")

def main():
    while True:
        print("\n--- Virtual Machine Monitor (virsh) ---")
        print("1. List VMs")
        print("2. Start VM")
        print("3. Stop VM")
        print("4. VM Status")
        print("5. Create VM from XML")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_vms()
        elif choice == '2':
            name = input("Enter VM name to start: ")
            start_vm(name)
        elif choice == '3':
            name = input("Enter VM name to stop: ")
            stop_vm(name)
        elif choice == '4':
            name = input("Enter VM name to check status: ")
            get_status(name)
        elif choice == '5':
            xml = input("Enter path to XML config (e.g., vm_template.xml): ")
            create_vm(xml)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
