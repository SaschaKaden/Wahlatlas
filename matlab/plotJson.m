addpath("../results");
close all;
format compact

names = {"chemnitz", "dresden", "leipzig", "mittelsachsen", "bautzen", "erzgebirge"};

for nameIndex = 1:length(names) 
    name = names{nameIndex};

    if name == "chemnitz"
        data = jsondecode(fileread("results/chemnitz.json"));
        scaleFactor = 0.5;
    elseif name == "dresden"
        data = jsondecode(fileread("results/Dresden.json"));
        scaleFactor = 0.5;
    elseif name == "landkreis_leipzig"
        data = jsondecode(fileread("results/landkreis leipzig.json"));
    elseif name == "leipzig"
        data = jsondecode(fileread("results/leipzig.json"));
        scaleFactor = 0.5;
    elseif name == "mittelsachsen"
        data = jsondecode(fileread("results/mittelsachsen.json"));
        scaleFactor = 0.1;
    elseif name == "bautzen"
        data = jsondecode(fileread("results/bautzen.json"));
        scaleFactor = 0.1;
    elseif name == "erzgebirge"
        data = jsondecode(fileread("results/erzgebirge.json"));
        scaleFactor = 0.1;
    end

    for i = 1:length(data)
      if isempty(data(i).pixel)
        data(i).pixel = 0;
      end
    end
    gridSize = 250; % 245

    v = zeros(length(data), 1) - 1;
    [potential, pixel, sinus, E, N] = deal(v, v, v, v, v);

    for i = 1:length(data)
        if data(i).gru_bt == 0
            continue;
        end
        [N(i), E(i)] = readID(data(i).id);
        potential(i) = data(i).potential_scale_wk / 100;
        pixel(i) = data(i).pixel;
        sinus(i) = readSinus(data(i).sinus);
    end
    % remove empty cells 
    N = N(N~=-1);
    E = E(E~=-1);
    potential = potential(potential~=-1);
    pixel = pixel(pixel~=-1);
    sinus = sinus(sinus~=-1);

    Z = pixel .* potential .* sinus;
    Z(Z==0) = NaN;
    zMax = max(Z) * scaleFactor;
    Z(Z>zMax) = zMax;

    % image colormap with export
    figure('WindowState','maximized');
    scatter(E, N, 20, Z, 'filled', 's')
    daspect([1 1 1]);
    colormap(jet);
    set(gca,'visible','off', 'Color', 'None'); 
    set(gca,'LooseInset',get(gca,'TightInset'));
    % exportgraphics(gca,'myplot.png','Resolution',300,'BackgroundColor','none') 

    % heatmap and excel export
    if false
        figure('WindowState', 'maximized');
        X = ((E - Emin) / gridSize) + 1;
        Y = ((N - Nmin) / gridSize) + 1;
        XYZ = [X Y Z];
        matXYZ = accumarray(XYZ(:,[2 1]), XYZ(:,3));
        h = heatmap(matXYZ, 'CellLabelColor','none');
        h.Colormap = jet; 
        % writematrix(matXYZ, 'testdata.xlsx', 'Sheet',1);
    end

    indices = find(isnan(Z));
    E(indices) = [];
    N(indices) = [];
    Z(indices) = [];
    
    Z = Z .* 10;
    jetMap = jet(max(round(Z)));
    c = strings(length(Z),1);
    c(:) = "0";
    for i = 1:length(c)
        for j = 1:length(jetMap)
            if round(Z(i)) == j
                c(i) = rgb2hex(jetMap(j,:));
            end
        end
    end
    ENZ = [E, N, c];
    fid = fopen('../results/' + name + '_ENZ.json','wt');
    fprintf(fid, jsonencode(ENZ));
    fclose(fid);
end