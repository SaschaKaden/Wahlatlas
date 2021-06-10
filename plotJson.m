data = jsondecode(fileread("Output.json"));
size = length(data);

X = zeros(size,1);
Y = zeros(size,1);
potential = zeros(size,1);
pixel = zeros(size,1);
gru_lt = zeros(size,1);
gru_bt = zeros(size,1);
sinus = zeros(size,1);

divider = 111320;
for i = 1:length(data)
    X(i) = data(i).lon / divider;
    Y(i) = data(i).lat / divider;
    potential(i) = data(i).potential;
    pixel(i) = data(i).pixel;
    gru_lt(i) = data(i).gru_lt;
    gru_bt(i) = data(i).gru_bt;
    sinus(i) = readSinus(data(i).sinus);
end

Z = (pixel/100 + potential) .* sinus .* gru_lt;

scatter(X,Y,100,Z, 'filled', 's')
daspect([1 1 1])
%axis tight; 
%set(gca,'visible','off')

% hold on
% I = imread('map.png'); 
% h = image(xlim,ylim,I); 
% uistack(h,'bottom')