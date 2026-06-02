@echo off

for %%f in (*.report) do (
    gpdcreport "%%f" -best 1 | gpec8 > "vs30_%%~nf.dat"
)