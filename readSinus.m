function [output] = readSinus(tag)
tag = string(tag);

if contains(tag, 'KET')
    output = 0.7;
elseif contains(tag, 'LIB')
    output = 1.3;
elseif contains(tag, 'PER')
    output = 1;
elseif contains(tag, 'EPE')
    output = 1.8;
elseif contains(tag, 'PRA')
    output = 1;
elseif contains(tag, 'SQK')
    output = 1.6;
elseif contains(tag, 'PRE')
    output = 0.4;
elseif contains(tag, 'BUM')
    output = 0.4;
elseif contains(tag, 'TRA')
    output = 0.6;
elseif contains(tag, 'HED')
    output = 1.2;
else
    output = 0;
end
    
end

