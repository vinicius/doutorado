latex article
bibtex article
latex article
latex article
dvips article.dvi -Ppdf -tletter -o article.ps
ps2pdf13 -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -dOptimize=true -dColorImageResolution=300 -dGrayImageResolution=300 -dMonoImageResolution=300 article.ps
evince article.pdf &
#acroread article.pdf &
