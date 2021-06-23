function [N, E] = readID(tag)

N = str2double(extractBetween(tag, "N", "E")) * 10;
E = str2double(extractAfter(tag, "E")) * 10;

end
