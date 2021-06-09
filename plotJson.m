data = jsondecode(fileread("Output.json"));
size = length(data);

X = zeros(size,1);
Y = zeros(size,1);
potential = zeros(size,1);
pixel = zeros(size,1);
gru_lt = zeros(size,1);
gru_bt = zeros(size,1);
sinus = zeros(size,1);

for i = 1:length(data)
    X(i) = data(i).lon / 1000;
    Y(i) = data(i).lat / 1000;
    potential(i) = data(i).potential;
    pixel(i) = data(i).pixel;
    gru_lt(i) = data(i).gru_lt;
    gru_bt(i) = data(i).gru_bt;
    sinus(i) = readSinus(data(i).sinus);
end

Z = (pixel/50 + potential) .* sinus;

figure
scatter(X,Y,40,Z, 'filled')
%axis tight; 
set(gca,'visible','off')

% hold on
% I = imread('map.png'); 
% h = image(xlim,ylim,I); 
% uistack(h,'bottom')