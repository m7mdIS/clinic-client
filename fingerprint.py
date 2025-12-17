from pyfingerprint.pyfingerprint import PyFingerprint
import time

PORT = '/dev/tty.usbserial-10'
BAUDRATE = 57600


def enroll_fingerprint():
    try:
        f = PyFingerprint(PORT, BAUDRATE, 0xFFFFFFFF, 0x00000000)

        if not f.verifyPassword():
            raise ValueError("Wrong fingerprint sensor password")

        print("✔ Sensor initialized")
        print("Place your finger on the sensor...")

        while not f.readImage():
            pass

        f.convertImage(0x01)

        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber >= 0:
            print("❌ Fingerprint already exists at position", positionNumber)
            return None

        print("Remove finger...")
        time.sleep(2)

        print("Place the SAME finger again...")
        while not f.readImage():
            pass

        f.convertImage(0x02)

        if not f.compareCharacteristics():
            print("❌ Fingerprints do not match")
            return None

        f.createTemplate()
        positionNumber = f.storeTemplate()

        print(f"✅ Fingerprint enrolled successfully (ID: {positionNumber})")
        return positionNumber

    except Exception as e:
        print("❌ Fingerprint error:", e)
        return None
