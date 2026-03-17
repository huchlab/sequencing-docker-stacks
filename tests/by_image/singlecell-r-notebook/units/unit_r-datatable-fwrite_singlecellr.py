from rpy2.robjects import r

r("""
library(data.table)
dt <- data.table(x = 1:3, y = c("a", "b", "c"))
tmp <- tempfile(fileext = ".tsv")
fwrite(dt, tmp)
stopifnot(file.exists(tmp))
""")
