
import subprocess
import platform
import socket

def get_network_devices_wmi():
    """Get network devices using WMI (Windows Management Instrumentation)"""
    try:
        import wmi
        c = wmi.WMI()
        print("=" * 60)
        print("NETWORK ADAPTERS (via WMI)")
        print("=" * 60)
        
        for interface in c.Win32_NetworkAdapter():
            if interface.NetConnectionID:  # Only show connected adapters
                print(f"\nName: {interface.Name}")
                print(f"Description: {interface.Description}")
                print(f"MAC Address: {interface.MACAddress}")
                print(f"Connection ID: {interface.NetConnectionID}")
                print(f"Status: {interface.NetConnectionStatus}")
                print(f"Speed: {interface.Speed}")
                print("-" * 40)
    except ImportError:
        print("WMI module not available. Install with: pip install WMI")
    except Exception as e:
        print(f"Error using WMI: {e}")

def get_network_devices_ipconfig():
    """Get network devices using ipconfig command"""
    try:
        print("\n" + "=" * 60)
        print("NETWORK CONFIGURATION (via ipconfig)")
        print("=" * 60)
        
        result = subprocess.run(['ipconfig', '/all'], 
                              capture_output=True, 
                              text=True, 
                              encoding='cp850')  # Windows console encoding
        print(result.stdout)
    except Exception as e:
        print(f"Error running ipconfig: {e}")

def get_network_devices_netsh():
    """Get network devices using netsh command"""
    try:
        print("\n" + "=" * 60)
        print("NETWORK INTERFACES (via netsh)")
        print("=" * 60)
        
        result = subprocess.run(['netsh', 'interface', 'show', 'interface'], 
                              capture_output=True, 
                              text=True,
                              encoding='cp850')
        print(result.stdout)
    except Exception as e:
        print(f"Error running netsh: {e}")

def get_network_devices_psutil():
    """Get network devices using psutil library"""
    try:
        import psutil
        print("\n" + "=" * 60)
        print("NETWORK INTERFACES (via psutil)")
        print("=" * 60)
        
        # Get network interface addresses
        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        
        for interface_name, interface_addresses in addrs.items():
            print(f"\nInterface: {interface_name}")
            
            # Get interface stats
            if interface_name in stats:
                stat = stats[interface_name]
                print(f"  Status: {'Up' if stat.isup else 'Down'}")
                print(f"  Speed: {stat.speed} Mbps")
                print(f"  MTU: {stat.mtu}")
            
            # Get addresses
            for addr in interface_addresses:
                if addr.family == socket.AF_INET:
                    print(f"  IPv4 Address: {addr.address}")
                    print(f"  Netmask: {addr.netmask}")
                elif addr.family == socket.AF_INET6:
                    print(f"  IPv6 Address: {addr.address}")
                elif addr.family == psutil.AF_LINK:
                    print(f"  MAC Address: {addr.address}")
            print("-" * 40)
    except ImportError:
        print("psutil module not available. Install with: pip install psutil")
    except Exception as e:
        print(f"Error using psutil: {e}")

# Main execution
if __name__ == "__main__":
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Hostname: {socket.gethostname()}")
    
    # Try different methods
    get_network_devices_netsh()
    # get_network_devices_ipconfig()
    # get_network_devices_psutil()
    # get_network_devices_wmi()
