import struct

def fast_inverse_sqrt(x):
    # Step 1: Convert float to raw binary (int)
    i = struct.unpack('i', struct.pack('f', x))[0]

    # Step 2: Apply the magic number and bit hack
    i = 0x5f3759df - (i >> 1)

    # Step 3: Convert bits back to float
    y = struct.unpack('f', struct.pack('i', i))[0]

    # Step 4: One iteration of Newton-Raphson method
    xhalf = 0.5 * x
    y = y * (1.5 - xhalf * y * y)

    return y

# Test
num = 4.0
print("1 / sqrt(4.0) =", fast_inverse_sqrt(num))  # Output should be close to 0.5
