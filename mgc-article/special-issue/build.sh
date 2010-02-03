latex cpe-vinicius
bibtex cpe-vinicius
latex cpe-vinicius
latex cpe-vinicius
dvips cpe-vinicius.dvi -Ppdf -tletter -o cpe-vinicius.ps
ps2pdf13 -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -dOptimize=true -dColorImageResolution=300 -dGrayImageResolution=300 -dMonoImageResolution=300 cpe-vinicius.ps
evince cpe-vinicius.pdf &
#acroread cpe-vinicius.pdf &
