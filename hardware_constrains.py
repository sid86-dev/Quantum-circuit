import cirq

device = cirq.google.Bristlecone

circuit = cirq.Circuit(device=device)

a0, a1 = cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
b0, b1 = cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)

circuit.append([cirq.CZ(a0, a1), cirq.CZ(b0, b1)])

print(circuit)