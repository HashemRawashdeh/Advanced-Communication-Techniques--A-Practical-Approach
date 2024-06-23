% Range of Eb/No values in dB
EbNo = -10:20;

% Preallocate matrix to store BER results
berSimResults = zeros(length(EbNo), 3);

% A preliminary simulation to calculate the signal power
simOut = sim('QAM64', 'ReturnWorkspaceOutputs', 'on');
modulatedSignal = simOut.get('modulatedSignal');

% Extract data from timeseries object
modulatedSignalData = modulatedSignal.Data;

% Calculate the average power of the modulated signal
signalPower = mean(abs(modulatedSignalData).^2);

% Loop over each Eb/No value
for i = 1:length(EbNo)
    % Set the AWGN channel parameters
    set_param('QAM64/AWGN Channel', 'EbNo', num2str(EbNo(i)));
    set_param('QAM64/AWGN Channel', 'SignalPower', num2str(signalPower));

    % Run the simulation with increased time and number of bits
    simOut = sim('QAM64', 'ReturnWorkspaceOutputs', 'on'); % Increase StopTime as needed

    % Extract the BER results
    berSim = simOut.get('berSim'); % Adjust if necessary to match your variable structure

    % Store the results in the preallocated matrix
    berSimResults(i, :) = berSim;
end

% Extract the simulated BER values
berSimulated = berSimResults(:, 1); % Extract the BER values (first column)

% Calculate the theoretical BER for 64-QAM
M = 64; % 64-QAM
berTheory = berawgn(EbNo, 'qam', M);

% Plotting the BER curves
figure;
semilogy(EbNo, berTheory, 'b-', 'LineWidth', 2); % Theoretical BER
hold on;
semilogy(EbNo, berSimulated, 'ro-', 'LineWidth', 2); % Simulated BER
grid on;
title('BER vs. Eb/No for 64-QAM');
xlabel('Eb/No (dB)');
ylabel('Bit Error Rate (BER)');
legend('Theoretical 64-QAM', 'Simulated 64-QAM');
hold off;
