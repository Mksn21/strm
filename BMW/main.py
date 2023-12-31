import streamlit as st
import streamlit.components.v1 as components
import serial
import sys
import glob


html_string = '''
<button>Request Serial Port</button>
<script>
  const button = document.querySelector('button');
  button.addEventListener('click', async function() {

    // Prompt user to select any serial port.
    const port = await navigator.serial.requestPort();
 port.open({ baudRate: 9600 });
    // Wait for the serial port to open.
  });

</script>
'''
html_string1 = '''
<button>Serial Port</button>
<script>
const reader = port.readable.getReader();

// Listen to data coming from the serial device.
while (true) {
  const { value, done } = reader.read();
  if (done) {
    // Allow the serial port to be closed later.
    reader.releaseLock();
    break;
  }
  // value is a Uint8Array.
  console.log(value);
}
</script>
'''

    
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

co = serial_ports()
if st.sidebar.button("add"):
  components.html(html_string)
  components.html(html_string1)
  st.write(co)
if st.button("as"): 
    st.write(co)
