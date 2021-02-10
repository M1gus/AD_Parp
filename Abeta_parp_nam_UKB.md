Parp mutations protect against mitochondrial toxicity in a Drosophila model of Alzheimer’s disease
================
Yizhou Yu, MRC Toxicology Unit, University of Cambridge,
(<yzy21@mrc-tox.cam.ac.uk>)
December 2020

# General information

This pipeline relates to data included in **Figure 2** to **Figure 12**
of out manuscript titled **Parp mutations protect against mitochondrial toxicity in a Drosophila model of Alzheimer’s disease**. It also contains additional
supplementary materials.

This pipeline aims to: <br> 1. Identify that the AD polygenic risk score
(PSQ) for AD is accurate: verify whether participants with the selected
SNPs have higher risk of AD. 2.

The input files for this analysis pipeline are on the master branch of
this GitHub page (link: <https://github.com/M1gus/AD_Parp>)

The UK Biobank data is not available in the repository as they require
separate application. Please visit ukbiobank.ac.uk for more information.
A detailed list of the variables used in the UK Biobank analysis is
available here:

**Supplementary Table 1. Variables from the UK Biobank**

``` r
library(stargazer)
stargazer(read.csv("data/metadt_Abeta_parp_nam_UKB.csv"), summary=FALSE, rownames=FALSE, type = "html")
```

<table style="text-align:center">

<tr>

<td colspan="10" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

my\_colname

</td>

<td>

FieldID

</td>

<td>

Field

</td>

<td>

Participants

</td>

<td>

ValueType

</td>

<td>

Units

</td>

<td>

Strata

</td>

<td>

Instances

</td>

<td>

Array

</td>

<td>

Coding

</td>

</tr>

<tr>

<td colspan="10" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

sleep\_dur

</td>

<td>

1,160

</td>

<td>

Sleep duration

</td>

<td>

501,636

</td>

<td>

Integer

</td>

<td>

hours/day

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,291

</td>

</tr>

<tr>

<td style="text-align:left">

wake

</td>

<td>

1,170

</td>

<td>

Getting up in morning

</td>

<td>

498,749

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,341

</td>

</tr>

<tr>

<td style="text-align:left">

chronotype

</td>

<td>

1,180

</td>

<td>

Morning/evening person (chronotype)

</td>

<td>

498,747

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,342

</td>

</tr>

<tr>

<td style="text-align:left">

nap

</td>

<td>

1,190

</td>

<td>

Nap during day

</td>

<td>

501,633

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,343

</td>

</tr>

<tr>

<td style="text-align:left">

insomnia

</td>

<td>

1,200

</td>

<td>

Sleeplessness / insomnia

</td>

<td>

501,632

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,343

</td>

</tr>

<tr>

<td style="text-align:left">

daysleep

</td>

<td>

1,220

</td>

<td>

Daytime dozing / sleeping (narcolepsy)

</td>

<td>

501,632

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

100,346

</td>

</tr>

<tr>

<td style="text-align:left">

birth

</td>

<td>

34

</td>

<td>

Year of birth

</td>

<td>

502,506

</td>

<td>

Integer

</td>

<td>

years

</td>

<td>

Primary

</td>

<td>

1

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

waist

</td>

<td>

48

</td>

<td>

Waist circumference

</td>

<td>

500,408

</td>

<td>

Continuous

</td>

<td>

cm

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

hip

</td>

<td>

49

</td>

<td>

Hip circumference

</td>

<td>

500,346

</td>

<td>

Continuous

</td>

<td>

cm

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

bpdias

</td>

<td>

4,079

</td>

<td>

Diastolic blood pressure, automated reading

</td>

<td>

475,129

</td>

<td>

Integer

</td>

<td>

mmHg

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

2

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

bpsys

</td>

<td>

4,080

</td>

<td>

Systolic blood pressure, automated reading

</td>

<td>

475,124

</td>

<td>

Integer

</td>

<td>

mmHg

</td>

<td>

Primary

</td>

<td>

4

</td>

<td>

2

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

sex

</td>

<td>

31

</td>

<td>

Sex

</td>

<td>

502,506

</td>

<td>

Categorical single

</td>

<td>

</td>

<td>

Primary

</td>

<td>

1

</td>

<td>

1

</td>

<td>

9

</td>

</tr>

<tr>

<td style="text-align:left">

tot\_p

</td>

<td>

30,860

</td>

<td>

Total protein

</td>

<td>

470,476

</td>

<td>

Continuous

</td>

<td>

</td>

<td>

Primary

</td>

<td>

2

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

189

</td>

<td>

Townsend deprivation index at recruitment

</td>

<td>

501,883

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

1

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

ethnicity

</td>

<td>

21,000

</td>

<td>

Ethnic background

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

3

</td>

<td>

1

</td>

<td>

1,001

</td>

</tr>

<tr>

<td style="text-align:left">

ad

</td>

<td>

42,021

</td>

<td>

Source of alzheimer’s disease report

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

1

</td>

<td>

1

</td>

<td>

300

</td>

</tr>

<tr>

<td style="text-align:left">

ad\_date

</td>

<td>

42,020

</td>

<td>

Date of alzheimer’s disease report

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

1

</td>

<td>

1

</td>

<td>

272

</td>

</tr>

<tr>

<td style="text-align:left">

edu\_level

</td>

<td>

6,138

</td>

<td>

Education and Qualifications

</td>

<td>

432,731

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

4

</td>

<td>

6

</td>

<td>

100,305

</td>

</tr>

<tr>

<td style="text-align:left">

vitamind

</td>

<td>

30,890

</td>

<td>

Vitamin D blood level

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

2

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

crp

</td>

<td>

30,710

</td>

<td>

c reactive protein, blood level

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

2

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td style="text-align:left">

date\_assessed

</td>

<td>

53

</td>

<td>

Date of attending assessment centre

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

</td>

<td>

4

</td>

<td>

1

</td>

<td>

</td>

</tr>

<tr>

<td colspan="10" style="border-bottom: 1px solid black">

</td>

</tr>

</table>

# Data curation

\#\# Load libraries

``` r
library(dplyr)
library(reshape)
library(corrplot)
library(RColorBrewer)
library(MASS)
library(Hmisc)
library(car)
```

## Curate UKB phenotype data

``` r
## import ukb data and rename variables
rawdt = read.csv("data/UKBdt.csv", na.strings=c("","NA"))
colnames(rawdt)
```

    ##  [1] "eid"        "X31.0.0"    "X34.0.0"    "X48.0.0"    "X48.1.0"   
    ##  [6] "X48.2.0"    "X48.3.0"    "X49.0.0"    "X49.1.0"    "X49.2.0"   
    ## [11] "X49.3.0"    "X53.0.0"    "X53.1.0"    "X53.2.0"    "X53.3.0"   
    ## [16] "X189.0.0"   "X1160.0.0"  "X1160.1.0"  "X1160.2.0"  "X1160.3.0" 
    ## [21] "X1170.0.0"  "X1170.1.0"  "X1170.2.0"  "X1170.3.0"  "X1180.0.0" 
    ## [26] "X1180.1.0"  "X1180.2.0"  "X1180.3.0"  "X1190.0.0"  "X1190.1.0" 
    ## [31] "X1190.2.0"  "X1190.3.0"  "X1200.0.0"  "X1200.1.0"  "X1200.2.0" 
    ## [36] "X1200.3.0"  "X1220.0.0"  "X1220.1.0"  "X1220.2.0"  "X1220.3.0" 
    ## [41] "X4079.0.0"  "X4079.0.1"  "X4079.1.0"  "X4079.1.1"  "X4079.2.0" 
    ## [46] "X4079.2.1"  "X4079.3.0"  "X4079.3.1"  "X4080.0.0"  "X4080.0.1" 
    ## [51] "X4080.1.0"  "X4080.1.1"  "X4080.2.0"  "X4080.2.1"  "X4080.3.0" 
    ## [56] "X4080.3.1"  "X6138.0.0"  "X6138.0.1"  "X6138.0.2"  "X6138.0.3" 
    ## [61] "X6138.0.4"  "X6138.0.5"  "X6138.1.0"  "X6138.1.1"  "X6138.1.2" 
    ## [66] "X6138.1.3"  "X6138.1.4"  "X6138.1.5"  "X6138.2.0"  "X6138.2.1" 
    ## [71] "X6138.2.2"  "X6138.2.3"  "X6138.2.4"  "X6138.2.5"  "X6138.3.0" 
    ## [76] "X6138.3.1"  "X6138.3.2"  "X6138.3.3"  "X6138.3.4"  "X6138.3.5" 
    ## [81] "X21000.0.0" "X21000.1.0" "X21000.2.0" "X30710.0.0" "X30710.1.0"
    ## [86] "X30860.0.0" "X30860.1.0" "X30890.0.0" "X30890.1.0" "X42020.0.0"
    ## [91] "X42021.0.0"

``` r
#aggregate the columns by selecting the last results, for each 
ukb_pheno_dt_t = melt(rawdt, id='eid')
# head(ukb_pheno_dt_t)

#order by variable to make sure I am will be replacing the latest value 
ukb_pheno_dt_t <- ukb_pheno_dt_t[order(ukb_pheno_dt_t$variable),] 

#delete everything after period 
ukb_pheno_dt_t$variable = gsub("\\..*","",ukb_pheno_dt_t$variable)

#aggregate by last 
ukb_t_na = na.omit(ukb_pheno_dt_t)
ukb_t_na = aggregate(ukb_t_na, by=list(ukb_t_na$eid,ukb_t_na$variable), FUN=tail, n = 1)

# Curate
ukb_t_na = ukb_t_na[c("eid", "variable", "value")]
ukb_t_na$variable = as.factor(ukb_t_na$variable)

# put it back straight 
ukb_cur = cast(ukb_t_na, eid~variable)
```

## Decode

The variables to decode are:

``` r
ukb_decode = ukb_cur
colnames(ukb_decode)
```

    ##  [1] "eid"    "X1160"  "X1170"  "X1180"  "X1190"  "X1200"  "X1220"  "X189"  
    ##  [9] "X21000" "X30710" "X30860" "X30890" "X31"    "X34"    "X4079"  "X4080" 
    ## [17] "X42020" "X42021" "X48"    "X49"    "X53"    "X6138"

``` r
ukb_decode = ukb_cur
lvl.100291 <- c(-3,-1)
lbl.100291 <- c("Prefer not to answer","Do not know")
ukb_decode$X1160 <- replace(ukb_decode$X1160, which(ukb_decode$X1160 < 0), NA)

lvl.100341 <- c(-3,-1,1,2,3,4)
lbl.100341 <- c("Prefer not to answer","Do not know","Not at all easy","Not very easy","Fairly easy","Very easy")
ukb_decode$X1170 <- ordered(ukb_decode$X1170, levels=lvl.100341, labels=lbl.100341)

lvl.100342 <- c(-3,-1,1,2,3,4)
lbl.100342 <- c("Prefer not to answer","Do not know","Definitely a \'morning\' person","More a \'morning\' than \'evening\' person","More an \'evening\' than a \'morning\' person","Definitely an \'evening\' person")
ukb_decode$X1180 <- ordered(ukb_decode$X1180, levels=lvl.100342, labels=lbl.100342)

lvl.100343 <- c(-3,1,2,3)
lbl.100343 <- c("Prefer not to answer","Never/rarely","Sometimes","Usually")
ukb_decode$X1190 <- ordered(ukb_decode$X1190, levels=lvl.100343, labels=lbl.100343)
ukb_decode$X1200 <- ordered(ukb_decode$X1200, levels=lvl.100343, labels=lbl.100343)

lvl.100346 <- c(-3,-1,0,1,2,3)
lbl.100346 <- c("Prefer not to answer","Do not know","Never/rarely","Sometimes","Often","All of the time")
ukb_decode$X1220 <- ordered(ukb_decode$X1220, levels=lvl.100346, labels=lbl.100346)

lvl.0009 <- c(0,1)
lbl.0009 <- c("Female","Male")
ukb_decode$X31 <- ordered(ukb_decode$X31, levels=lvl.0009, labels=lbl.0009)

lvl.0300 <- c(0,1,2)
lbl.0300 <- c("Self-reported only","Hospital admission","Death only")
lvl.0272 <- c(1)
lbl.0272 <- c("Date is unknown")
ukb_decode$X42021 <- ordered(ukb_decode$X42021, levels=lvl.0300, labels=lbl.0300)
ukb_decode$X42020 <- ordered(ukb_decode$X42020, levels=lvl.0272, labels=lbl.0272)

lvl.1001 <- c(-3,-1,1,2,3,4,5,6,1001,1002,1003,2001,2002,2003,2004,3001,3002,3003,3004,4001,4002,4003)
lbl.1001 <- c("Prefer not to answer","Do not know","White","Mixed","Asian or Asian British","Black or Black British","Chinese","Other ethnic group","British","Irish","Any other white background","White and Black Caribbean","White and Black African","White and Asian","Any other mixed background","Indian","Pakistani","Bangladeshi","Any other Asian background","Caribbean","African","Any other Black background")
ukb_decode$X21000 <- ordered(ukb_decode$X21000, levels=lvl.1001, labels=lbl.1001)

lvl.100305 <- c(-7,-3,1,2,3,4,5,6)
lbl.100305 <- c("None of the above","Prefer not to answer","College or University degree","A levels/AS levels or equivalent","O levels/GCSEs or equivalent","CSEs or equivalent","NVQ or HND or HNC or equivalent","Other professional qualifications eg: nursing, teaching")
ukb_decode$X6138 <- ordered(ukb_decode$X6138, levels=lvl.100305, labels=lbl.100305)
```

## Fix column names

Replace column names with good variables

``` r
UKBdt_colname_df = data.frame(col = colnames(ukb_decode)[-1])

meta_dt = read.csv("data/metadt_Abeta_parp_nam_UKB.csv")
meta_dt$FieldID = paste("X", meta_dt$FieldID, sep = "")

#join allows orders to be kept 
#library(plyr)
UKBdt_col_df_mer = merge(UKBdt_colname_df, meta_dt, by.x = "col", by.y = "FieldID")

colnames(ukb_decode) <- c("eid", UKBdt_col_df_mer$my_colname)
```

\#\# Curate variables

``` r
ukb_curate = ukb_decode

ukb_curate = ukb_curate %>%
  mutate(ad_diag = c("FALSE", "TRUE")[(!is.na(ad_date) | 
                                     !is.na(ad) 
                                     )+1] )

# curate age -> first 4 variables of TGA assay date
ukb_curate$age <- substr(ukb_curate$date_assessed,1,4)
ukb_curate$age <- as.numeric(ukb_curate$age) - as.numeric(ukb_curate$birth)

#create whr
ukb_curate$whr = as.numeric(ukb_curate$waist) / as.numeric(ukb_curate$hip)

#normalise blood markers by protein level
ukb_curate$log_normCRP = log(as.numeric(ukb_curate$crp)/as.numeric(ukb_curate$tot_p))
ukb_curate$log_normVitaD = log(as.numeric(ukb_curate$vitamind)/as.numeric(ukb_curate$tot_p))

#make the rest into numeric
ukb_curate$townsend = as.numeric(ukb_curate$townsend) 
ukb_curate$crp=as.numeric(ukb_curate$crp)
ukb_curate$vitamind=as.numeric(ukb_curate$vitamind)
ukb_curate$tot_p=as.numeric(ukb_curate$tot_p)
ukb_curate$sleep_dur = as.numeric(ukb_curate$sleep_dur)
ukb_curate$waist=as.numeric(ukb_curate$waist)
ukb_curate$hip=as.numeric(ukb_curate$hip)

ukb_curate$date_assessed = as.Date(ukb_curate$date_assessed)

ukb_curate$birth = as.numeric(ukb_curate$birth)

ukb_curate$bpdias = as.numeric(ukb_curate$bpdias)
ukb_curate$bpsys = as.numeric(ukb_curate$bpsys)

write.csv(ukb_curate, "data_out/ukb_dt_curated.csv", row.names = F)
```

## Descriptive statistics: phenotypes

``` r
library(arsenal)
```

    ## 
    ## Attaching package: 'arsenal'

    ## The following object is masked from 'package:Hmisc':
    ## 
    ##     %nin%

``` r
#delete first column -> eid
ukb_descript_stats <- tableby(ad_diag ~ ., data = ukb_curate[,2:ncol(ukb_curate)])
write2word(ukb_descript_stats, "ukb_descriptStats.doc",
  keep.md = TRUE,
  quiet = TRUE, # passed to rmarkdown::render
  title = "Descriptive statistics of the UK Biobank subcohort analysed") # passed to summary.tableby
```

## Curate SNP data

\#\#\# Load data

``` r
library(BGData)
```

    ## Loading required package: BEDMatrix

    ## Loading required package: LinkedMatrix

    ## Loading required package: symDMatrix

    ## 
    ## Attaching package: 'BGData'

    ## The following object is masked from 'package:Hmisc':
    ## 
    ##     summarize

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     summarize

``` r
library(BGLR)
library(data.table) #requires brew update && brew install llvm
```

    ## 
    ## Attaching package: 'data.table'

    ## The following object is masked from 'package:reshape':
    ## 
    ##     melt

    ## The following objects are masked from 'package:dplyr':
    ## 
    ##     between, first, last

``` r
library(qqman)
```

    ## 

    ## For example usage please run: vignette('qqman')

    ## 

    ## Citation appreciated but not required:

    ## Turner, S.D. qqman: an R package for visualizing GWAS results using Q-Q and manhattan plots. biorXiv DOI: 10.1101/005165 (2014).

    ## 

    ## 
    ## Attaching package: 'qqman'

    ## The following object is masked from 'package:lattice':
    ## 
    ##     qq

``` r
#Load each chromosome as a BEDMatrix object and link them by columns to a ColumnLinkedMatrix object:
genoPath = "~/data_repository/UKB_dt_18-4-2020/"
full_ukb_gen_dt <- as.ColumnLinkedMatrix(lapply(c(1:22), function(chrom) {
  BEDMatrix(paste0(genoPath, "ukb_cal_chr", chrom,"_v2.bed"))
}))
```

    ## Extracting number of samples and rownames from ukb_cal_chr1_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr1_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr2_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr2_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr3_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr3_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr4_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr4_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr5_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr5_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr6_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr6_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr7_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr7_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr8_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr8_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr9_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr9_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr10_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr10_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr11_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr11_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr12_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr12_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr13_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr13_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr14_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr14_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr15_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr15_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr16_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr16_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr17_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr17_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr18_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr18_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr19_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr19_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr20_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr20_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr21_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr21_v2.bim...

    ## Extracting number of samples and rownames from ukb_cal_chr22_v2.fam...

    ## Extracting number of variants and colnames from ukb_cal_chr22_v2.bim...

``` r
rownames(full_ukb_gen_dt) <- sapply(strsplit(rownames(full_ukb_gen_dt), "_"), `[`, 1) 
# convert names from FID_II D to eid

#Combine genotypes and phenotypes into a BGData object
full_pheno_geno_dt <- as.BGData(full_ukb_gen_dt, alternatePhenotypeFile = "data_out/ukb_dt_curated.csv")
```

    ## Extracting phenotypes from .fam file, assuming that the .fam file of the first BEDMatrix instance is representative of all the other nodes...

    ## Extracting map from .bim files...

    ## Merging alternate phenotype file...

``` r
allSamples <- rownames(full_pheno_geno_dt@geno)
#488377 samples
allVariants <- colnames(full_pheno_geno_dt@geno)
#784256 variants
save(full_pheno_geno_dt, file = "data_out/full_pheno_geno_dt.RData")
```

\#\#\# Summary statistics

``` r
# Compute summary statistics for each variant among all white British samples 
#full_pheno_geno_summary <- summarize(full_pheno_geno_dt@geno, j = allVariants, chunkSize = 2500, nCores = 8)
#save(full_pheno_geno_summary, file = "data_out/full_pheno_geno_summary.RData")
```

### PARP SNPs

All PARP snps were obtained from <https://www.ncbi.nlm.nih.gov/snp>,
using the search code PARP1\[Gene Name\] AND “Homo sapiens”\[Organism\]
<br> A total of 13341 SNPs were obtained for PARP1, where 12701 of them
were unique. and Y of them were present in the UK Biobank.

``` r
parp_snp_dt = read.csv("data/PARP_snp_result.txt", sep = "\t")
parp_snp_dt$snp = paste0("rs",parp_snp_dt$snp_id)
length(parp_snp_dt$snp)
```

    ## [1] 13341

``` r
length(unique(parp_snp_dt$snp))
```

    ## [1] 12701

``` r
# Select variants 
full_pheno_geno_summary = load("data_out/full_pheno_geno_summary.RData")

parp_snp = unique(parp_snp_dt$snp)

# check all variants
ukbSNP_without_variant = gsub("_.*","",allVariants)
parp_intersect = intersect(parp_snp,ukbSNP_without_variant)

#get the index values 
parp_intersect_intersect_i_df = data.frame(row_num = 1:length(allVariants), 
                                          raw_var = allVariants, 
                                          SNP_only = ukbSNP_without_variant, 
                                          selected_var = ukbSNP_without_variant %in% parp_intersect)

parp_intersect_intersect_i_df = subset(parp_intersect_intersect_i_df, selected_var == TRUE)

parp_snp_dt = merge(parp_snp_dt[!duplicated(parp_snp_dt$snp),], parp_intersect_intersect_i_df,
                              by.x="snp", by.y = "SNP_only")

write.csv(parp_snp_dt,"data_out/parp_variants_found_in_ukbdt.csv", row.names = FALSE)

BGD_parp_variants = full_pheno_geno_dt@geno[,na.omit(parp_snp_dt$raw_var)]

save(BGD_parp_variants, file = "data_out/parp_variants_dt.RData")
```

### AD SNPs

``` r
AD_snp_file = read.csv("data/metadt_AD_snp.csv")

# check all variants
AD_intersect = intersect(unique(AD_snp_file$snp),ukbSNP_without_variant)

#get the index values 
AD_intersect_intersect_i_df = data.frame(row_num = 1:length(allVariants), 
                                          raw_var = allVariants, 
                                          SNP_only = ukbSNP_without_variant, 
                                          selected_var = ukbSNP_without_variant %in% AD_intersect)

AD_intersect_intersect_i_df = subset(AD_intersect_intersect_i_df, selected_var == TRUE)

AD_snp_file = merge(AD_snp_file, AD_intersect_intersect_i_df,
                              by.x="snp", by.y = "SNP_only")

write.csv(AD_snp_file,"data_out/AD_variants_found_in_ukbdt.csv", row.names = FALSE)

BGD_AD_variants = full_pheno_geno_dt@geno[,na.omit(AD_snp_file$raw_var)]

save(BGD_AD_variants, file = "data_out/AD_variants_dt.RData")
```

*Save all 3 datasets together*

``` r
AD_variants_df = as.data.frame(BGD_AD_variants)
AD_variants_df$eid = rownames(AD_variants_df)

parp_variants_df = as.data.frame(BGD_parp_variants)
parp_variants_df$eid = rownames(parp_variants_df)

full_snp_dt = merge(AD_variants_df,parp_variants_df, by = "eid")

ukb_curate = read.csv("data_out/ukb_dt_curated.csv")

ukb_dt = merge(ukb_curate,full_snp_dt, by = "eid", all.x = TRUE)

write.csv(ukb_dt, "data_out/ukb_dt_curated_addedSNP.csv", row.names = F)
```

## Alzheimer’s disease: polygenic risk score validation

\#\#\# Correlation table

``` r
#select numeric data 
numeric_cols <- unlist(lapply(ukb_dt, is.numeric))  
ukb_dt_numeric = ukb_dt[,numeric_cols]
ukb_correl<-rcorr(as.matrix(ukb_dt_numeric[,2:ncol(ukb_dt_numeric)]))

#pdf(file = "fig_out/summary_stats_corrplot.pdf")
corrplot(ukb_correl$r, type="upper", p.mat = ukb_correl$P, sig.level = 0.01, insig = "blank",
         col=brewer.pal(n=8, name="RdYlBu"))
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

``` r
#dev.off()
```

### Validation models

\#\#\#\# Additional data curation: BP, education, ethnicity

``` r
ukb_dt = read.csv("data_out/ukb_dt_curated_addedSNP.csv")

ukb_dt$edu = ifelse(ukb_dt$edu_level == "None of the above" | ukb_dt$edu_level == "Prefer not to answer", "No certificate", "Certificate")
ukb_dt$ethnicity_sim = ifelse(ukb_dt$ethnicity == "British", "British", "Minority")

# recode levels to numeric

ukb_dt$wake_sim = as.numeric(mgsub::mgsub(string = ukb_dt$wake, pattern = c("Prefer not to answer","Do not know","Not at all easy","Not very easy","Fairly easy","Very easy"),
                               replacement = c(NA,NA,0,1,2,3)))

ukb_dt$morningness_sim = mgsub::mgsub(string = ukb_dt$chronotype, pattern = c("Prefer not to answer","Do not know","Definitely an 'evening' person","More an ‘evening’ than a ‘morning’ person","More a ‘morning’ than ‘evening’ person","Definitely a ‘morning’ person"),
                               replacement = c(NA,NA,0,1,2,3))

ukb_dt$nap_sim = as.numeric(mgsub::mgsub(string = ukb_dt$nap, pattern = c("Prefer not to answer","Never/rarely","Sometimes","Usually"),
                               replacement = c(NA,0,1,2)))

ukb_dt$insomnia_sim = as.numeric(mgsub::mgsub(string = ukb_dt$insomnia, pattern = c("Prefer not to answer","Never/rarely","Sometimes","Usually"),
                               replacement = c(NA,0,1,2)))


ukb_dt$daysleep_sim = as.numeric(mgsub::mgsub(string = ukb_dt$daysleep, pattern = c("Prefer not to answer","Do not know","Never/rarely","Sometimes","Often","All of the time"),
                               replacement = c(NA,NA,0,1,2,3)))


ukb_dt$highBP[ukb_dt$bpdias>=90 | ukb_dt$bpsys>=140] <-1
ukb_dt$highBP[ukb_dt$bpdias<90 | ukb_dt$bpsys<140] <-0

write.csv(ukb_dt, "data_out/ukb_dt_curated_addedSNP_fixedVars.csv", row.names = F)
```

\#\#\#\# Phenotypic model

``` r
dt_AD_validation_model_1 = subset(ukb_dt, select = c(ad_diag, sleep_dur, daysleep_sim, nap_sim, insomnia_sim, 
                             wake_sim, morningness_sim, townsend, ethnicity_sim, whr, sex, age, 
                             log_normVitaD, log_normCRP, edu, highBP))

AD_validation_model_1= glm(data = na.omit(dt_AD_validation_model_1), ad_diag ~ sleep_dur + daysleep_sim +nap_sim+insomnia_sim+
                             wake_sim+morningness_sim+townsend+ethnicity_sim+whr + sex + age+
                             log_normVitaD+log_normCRP+edu+highBP, family = 'binomial')
summary(AD_validation_model_1)
```

Call: glm(formula = ad\_diag \~ sleep\_dur + daysleep\_sim + nap\_sim +
insomnia\_sim + wake\_sim + morningness\_sim + townsend + ethnicity\_sim
+ whr + sex + age + log\_normVitaD + log\_normCRP + edu + highBP, family
= “binomial”, data = na.omit(dt\_AD\_validation\_model\_1))

Deviance Residuals: Min 1Q Median 3Q Max  
\-0.3976 -0.0691 -0.0464 -0.0290 4.1297

Coefficients: Estimate Std. Error (Intercept) -14.792153 0.739331
sleep\_dur 0.102587 0.035382 daysleep\_sim 0.294098 0.074165 nap\_sim
-0.034791 0.069742 insomnia\_sim -0.393319 0.058277 wake\_sim -0.032816
0.060697 morningness\_simDefinitely a ‘morning’ person 0.110462 0.171406
morningness\_simMore a ‘morning’ than ‘evening’ person 0.094537 0.164260
morningness\_simMore an ‘evening’ than a ‘morning’ person -0.064052
0.166238 townsend 0.046175 0.013084 ethnicity\_simMinority -0.134097
0.142742 whr -0.175494 0.622138 sexMale 0.092390 0.110033 age 0.121408
0.006334 log\_normVitaD -0.204788 0.086265 log\_normCRP -0.111515
0.041013 eduNo certificate 0.697601 0.085069 highBP 0.087890 0.100296 z
value Pr(\>|z|)  
(Intercept) -20.007 \< 2e-16 *** sleep\_dur 2.899 0.003739 **
daysleep\_sim 3.965 7.33e-05 *** nap\_sim -0.499 0.617881  
insomnia\_sim -6.749 1.49e-11 *** wake\_sim -0.541 0.588747  
morningness\_simDefinitely a ‘morning’ person 0.644 0.519286  
morningness\_simMore a ‘morning’ than ‘evening’ person 0.576 0.564932  
morningness\_simMore an ‘evening’ than a ‘morning’ person -0.385
0.700011  
townsend 3.529 0.000417 *** ethnicity\_simMinority -0.939 0.347507  
whr -0.282 0.777880  
sexMale 0.840 0.401100  
age 19.168 \< 2e-16 *** log\_normVitaD -2.374 0.017599 *  
log\_normCRP -2.719 0.006548 \*\* eduNo certificate 8.200 2.40e-16
\*\*\* highBP 0.876 0.380863  
— Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 9390  on 344288  degrees of freedom

Residual deviance: 8683 on 344271 degrees of freedom AIC: 8719

Number of Fisher Scoring iterations: 10

``` r
vif(AD_validation_model_1)
```

``` 
                GVIF Df GVIF^(1/(2*Df))
```

sleep\_dur 1.100636 1 1.049112 daysleep\_sim 1.209198 1 1.099635
nap\_sim 1.276973 1 1.130032 insomnia\_sim 1.111618 1 1.054333 wake\_sim
1.316906 1 1.147565 morningness\_sim 1.264674 3 1.039912 townsend
1.110387 1 1.053749 ethnicity\_sim 1.053967 1 1.026629 whr 2.006988 1
1.416682 sex 1.938277 1 1.392220 age 1.083860 1 1.041086 log\_normVitaD
1.074235 1 1.036453 log\_normCRP 1.117972 1 1.057342 edu 1.093073 1
1.045502 highBP 1.020873 1 1.010382

``` r
stargazer::stargazer(AD_validation_model_1,type="html",out = "fig_out/AD_validation_model_noSNPmodel.html",
          dep.var.labels="AD diagnosis or not",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

AD diagnosis or not

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

sleep\_dur

</td>

<td>

0.103<sup>\*\*\*</sup> (0.035)

</td>

</tr>

<tr>

<td style="text-align:left">

daysleep\_sim

</td>

<td>

0.294<sup>\*\*\*</sup> (0.074)

</td>

</tr>

<tr>

<td style="text-align:left">

nap\_sim

</td>

<td>

\-0.035 (0.070)

</td>

</tr>

<tr>

<td style="text-align:left">

insomnia\_sim

</td>

<td>

\-0.393<sup>\*\*\*</sup> (0.058)

</td>

</tr>

<tr>

<td style="text-align:left">

wake\_sim

</td>

<td>

\-0.033 (0.061)

</td>

</tr>

<tr>

<td style="text-align:left">

morningness\_simDefinitely a ‘morning’ person

</td>

<td>

0.110 (0.171)

</td>

</tr>

<tr>

<td style="text-align:left">

morningness\_simMore a ‘morning’ than ‘evening’ person

</td>

<td>

0.095 (0.164)

</td>

</tr>

<tr>

<td style="text-align:left">

morningness\_simMore an ‘evening’ than a ‘morning’ person

</td>

<td>

\-0.064 (0.166)

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

0.046<sup>\*\*\*</sup> (0.013)

</td>

</tr>

<tr>

<td style="text-align:left">

ethnicity\_simMinority

</td>

<td>

\-0.134 (0.143)

</td>

</tr>

<tr>

<td style="text-align:left">

whr

</td>

<td>

\-0.175 (0.622)

</td>

</tr>

<tr>

<td style="text-align:left">

sexMale

</td>

<td>

0.092 (0.110)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.121<sup>\*\*\*</sup> (0.006)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.205<sup>\*\*</sup> (0.086)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

\-0.112<sup>\*\*\*</sup> (0.041)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.698<sup>\*\*\*</sup> (0.085)

</td>

</tr>

<tr>

<td style="text-align:left">

highBP

</td>

<td>

0.088 (0.100)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

\-14.792<sup>\*\*\*</sup> (0.739)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

344,289

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-4,341.507

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

8,719.015

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

``` r
stepAIC(AD_validation_model_1)
```

    ## Start:  AIC=8719.01
    ## ad_diag ~ sleep_dur + daysleep_sim + nap_sim + insomnia_sim + 
    ##     wake_sim + morningness_sim + townsend + ethnicity_sim + whr + 
    ##     sex + age + log_normVitaD + log_normCRP + edu + highBP
    ## 
    ##                   Df Deviance    AIC
    ## - morningness_sim  3   8685.9 8715.9
    ## - whr              1   8683.1 8717.1
    ## - nap_sim          1   8683.3 8717.3
    ## - wake_sim         1   8683.3 8717.3
    ## - sex              1   8683.7 8717.7
    ## - highBP           1   8683.8 8717.8
    ## - ethnicity_sim    1   8683.9 8717.9
    ## <none>                 8683.0 8719.0
    ## - log_normVitaD    1   8688.6 8722.6
    ## - log_normCRP      1   8690.5 8724.5
    ## - sleep_dur        1   8691.3 8725.3
    ## - townsend         1   8695.1 8729.1
    ## - daysleep_sim     1   8698.1 8732.1
    ## - insomnia_sim     1   8729.0 8763.0
    ## - edu              1   8746.4 8780.4
    ## - age              1   9101.4 9135.4
    ## 
    ## Step:  AIC=8715.89
    ## ad_diag ~ sleep_dur + daysleep_sim + nap_sim + insomnia_sim + 
    ##     wake_sim + townsend + ethnicity_sim + whr + sex + age + log_normVitaD + 
    ##     log_normCRP + edu + highBP
    ## 
    ##                 Df Deviance    AIC
    ## - wake_sim       1   8685.9 8713.9
    ## - whr            1   8686.0 8714.0
    ## - nap_sim        1   8686.1 8714.1
    ## - sex            1   8686.5 8714.5
    ## - highBP         1   8686.6 8714.6
    ## - ethnicity_sim  1   8686.7 8714.7
    ## <none>               8685.9 8715.9
    ## - log_normVitaD  1   8691.3 8719.3
    ## - log_normCRP    1   8693.6 8721.6
    ## - sleep_dur      1   8693.9 8721.9
    ## - townsend       1   8698.0 8726.0
    ## - daysleep_sim   1   8701.3 8729.3
    ## - insomnia_sim   1   8731.3 8759.3
    ## - edu            1   8750.6 8778.6
    ## - age            1   9103.3 9131.3
    ## 
    ## Step:  AIC=8713.9
    ## ad_diag ~ sleep_dur + daysleep_sim + nap_sim + insomnia_sim + 
    ##     townsend + ethnicity_sim + whr + sex + age + log_normVitaD + 
    ##     log_normCRP + edu + highBP
    ## 
    ##                 Df Deviance    AIC
    ## - whr            1   8686.0 8712.0
    ## - nap_sim        1   8686.1 8712.1
    ## - sex            1   8686.5 8712.5
    ## - highBP         1   8686.6 8712.6
    ## - ethnicity_sim  1   8686.8 8712.8
    ## <none>               8685.9 8713.9
    ## - log_normVitaD  1   8691.3 8717.3
    ## - log_normCRP    1   8693.6 8719.6
    ## - sleep_dur      1   8693.9 8719.9
    ## - townsend       1   8698.0 8724.0
    ## - daysleep_sim   1   8701.3 8727.3
    ## - insomnia_sim   1   8732.3 8758.3
    ## - edu            1   8750.9 8776.9
    ## - age            1   9117.8 9143.8
    ## 
    ## Step:  AIC=8711.98
    ## ad_diag ~ sleep_dur + daysleep_sim + nap_sim + insomnia_sim + 
    ##     townsend + ethnicity_sim + sex + age + log_normVitaD + log_normCRP + 
    ##     edu + highBP
    ## 
    ##                 Df Deviance    AIC
    ## - nap_sim        1   8686.2 8710.2
    ## - sex            1   8686.6 8710.6
    ## - highBP         1   8686.7 8710.7
    ## - ethnicity_sim  1   8686.9 8710.9
    ## <none>               8686.0 8712.0
    ## - log_normVitaD  1   8691.3 8715.3
    ## - sleep_dur      1   8694.0 8718.0
    ## - log_normCRP    1   8694.7 8718.7
    ## - townsend       1   8698.0 8722.0
    ## - daysleep_sim   1   8701.4 8725.4
    ## - insomnia_sim   1   8732.5 8756.5
    ## - edu            1   8750.9 8774.9
    ## - age            1   9121.4 9145.4
    ## 
    ## Step:  AIC=8710.2
    ## ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + townsend + 
    ##     ethnicity_sim + sex + age + log_normVitaD + log_normCRP + 
    ##     edu + highBP
    ## 
    ##                 Df Deviance    AIC
    ## - sex            1   8686.7 8708.7
    ## - highBP         1   8686.9 8708.9
    ## - ethnicity_sim  1   8687.1 8709.1
    ## <none>               8686.2 8710.2
    ## - log_normVitaD  1   8691.4 8713.4
    ## - sleep_dur      1   8694.0 8716.0
    ## - log_normCRP    1   8695.0 8717.0
    ## - townsend       1   8698.1 8720.1
    ## - daysleep_sim   1   8702.3 8724.3
    ## - insomnia_sim   1   8733.3 8755.3
    ## - edu            1   8751.0 8773.0
    ## - age            1   9123.7 9145.7
    ## 
    ## Step:  AIC=8708.73
    ## ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + townsend + 
    ##     ethnicity_sim + age + log_normVitaD + log_normCRP + edu + 
    ##     highBP
    ## 
    ##                 Df Deviance    AIC
    ## - highBP         1   8687.6 8707.6
    ## - ethnicity_sim  1   8687.6 8707.6
    ## <none>               8686.7 8708.7
    ## - log_normVitaD  1   8691.9 8711.9
    ## - sleep_dur      1   8694.5 8714.5
    ## - log_normCRP    1   8695.8 8715.8
    ## - townsend       1   8698.7 8718.7
    ## - daysleep_sim   1   8703.3 8723.3
    ## - insomnia_sim   1   8736.0 8756.0
    ## - edu            1   8751.4 8771.4
    ## - age            1   9128.2 9148.2
    ## 
    ## Step:  AIC=8707.58
    ## ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + townsend + 
    ##     ethnicity_sim + age + log_normVitaD + log_normCRP + edu
    ## 
    ##                 Df Deviance    AIC
    ## - ethnicity_sim  1   8688.5 8706.5
    ## <none>               8687.6 8707.6
    ## - log_normVitaD  1   8692.9 8710.9
    ## - sleep_dur      1   8695.4 8713.4
    ## - log_normCRP    1   8696.4 8714.4
    ## - townsend       1   8699.5 8717.5
    ## - daysleep_sim   1   8704.0 8722.0
    ## - insomnia_sim   1   8737.1 8755.1
    ## - edu            1   8752.8 8770.8
    ## - age            1   9129.0 9147.0
    ## 
    ## Step:  AIC=8706.47
    ## ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + townsend + 
    ##     age + log_normVitaD + log_normCRP + edu
    ## 
    ##                 Df Deviance    AIC
    ## <none>               8688.5 8706.5
    ## - log_normVitaD  1   8693.4 8709.4
    ## - sleep_dur      1   8696.4 8712.4
    ## - log_normCRP    1   8697.1 8713.1
    ## - townsend       1   8699.7 8715.7
    ## - daysleep_sim   1   8704.6 8720.6
    ## - insomnia_sim   1   8737.6 8753.6
    ## - edu            1   8754.6 8770.6
    ## - age            1   9134.6 9150.6

    ## 
    ## Call:  glm(formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    ##     townsend + age + log_normVitaD + log_normCRP + edu, family = "binomial", 
    ##     data = na.omit(dt_AD_validation_model_1))
    ## 
    ## Coefficients:
    ##       (Intercept)          sleep_dur       daysleep_sim       insomnia_sim  
    ##         -14.90665            0.09879            0.28304           -0.39825  
    ##          townsend                age      log_normVitaD        log_normCRP  
    ##           0.04384            0.12125           -0.19036           -0.11535  
    ## eduNo certificate  
    ##           0.70691  
    ## 
    ## Degrees of Freedom: 344288 Total (i.e. Null);  344280 Residual
    ## Null Deviance:       9390 
    ## Residual Deviance: 8688  AIC: 8706

Comparison: <br> Before: glm(data =
na.omit(dt\_AD\_validation\_model\_1), ad\_diag \~ sleep\_dur +
daysleep\_sim +nap\_sim+insomnia\_sim+
wake\_sim+morningness\_sim+townsend+ethnicity\_sim+whr + sex + age+
log\_normVitaD+log\_normCRP+edu+highBP, family = ‘binomial’)

After: glm(formula = ad\_diag \~ sleep\_dur + daysleep\_sim +
insomnia\_sim + townsend + age + log\_normVitaD + log\_normCRP + edu,
family = “binomial”, data = na.omit(dt\_AD\_validation\_model\_1))

``` r
AD_validation_model_simplified = glm(formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu, family = "binomial", 
    data = dt_AD_validation_model_1)
summary(AD_validation_model_simplified)
```

Call: glm(formula = ad\_diag \~ sleep\_dur + daysleep\_sim +
insomnia\_sim + townsend + age + log\_normVitaD + log\_normCRP + edu,
family = “binomial”, data = dt\_AD\_validation\_model\_1)

Deviance Residuals: Min 1Q Median 3Q Max  
\-0.4012 -0.0704 -0.0472 -0.0294 4.1910

Coefficients: Estimate Std. Error z value Pr(\>|z|)  
(Intercept) -15.239078 0.461484 -33.022 \< 2e-16 *** sleep\_dur 0.123478
0.030903 3.996 6.45e-05 *** daysleep\_sim 0.305920 0.061404 4.982
6.29e-07 *** insomnia\_sim -0.366588 0.051499 -7.118 1.09e-12 ***
townsend 0.033948 0.011734 2.893 0.003814 \*\* age 0.121995 0.005628
21.677 \< 2e-16 *** log\_normVitaD -0.183456 0.076593 -2.395 0.016611
*  
log\_normCRP -0.137928 0.035831 -3.849 0.000118 *** eduNo certificate
0.706211 0.076193 9.269 \< 2e-16 *\*\* — Signif. codes: 0 ‘***’ 0.001
’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 11402  on 405663  degrees of freedom

Residual deviance: 10537 on 405655 degrees of freedom (96840
observations deleted due to missingness) AIC: 10555

Number of Fisher Scoring iterations: 10

``` r
stargazer::stargazer(AD_validation_model_simplified,type="html",out = "fig_out/AD_validation_model_noSNPmodel_simplified.html",
          dep.var.labels="AD diagnosis or not",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

AD diagnosis or not

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

sleep\_dur

</td>

<td>

0.123<sup>\*\*\*</sup> (0.031)

</td>

</tr>

<tr>

<td style="text-align:left">

daysleep\_sim

</td>

<td>

0.306<sup>\*\*\*</sup> (0.061)

</td>

</tr>

<tr>

<td style="text-align:left">

insomnia\_sim

</td>

<td>

\-0.367<sup>\*\*\*</sup> (0.051)

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

0.034<sup>\*\*\*</sup> (0.012)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.122<sup>\*\*\*</sup> (0.006)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.183<sup>\*\*</sup> (0.077)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

\-0.138<sup>\*\*\*</sup> (0.036)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.706<sup>\*\*\*</sup> (0.076)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

\-15.239<sup>\*\*\*</sup> (0.461)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

405,664

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-5,268.693

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

10,555.390

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

#### AD PSG generation

Validation with all the above variables

``` r
rs10808026_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs10808026_C)

rs10933431_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs10933431_G)

rs11257238_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs11257238_T)

rs117618017_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs117618017_C)

rs12539172_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs12539172_T)

rs12590654_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs12590654_G)

rs138190086_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs138190086_G)

rs17125924_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs17125924_A)

rs190982_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs190982_G)

rs2632516_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs2632516_G)

rs3752246_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs3752246_G)

rs3851179_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs3851179_T)

rs3865444_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs3865444_C)

rs41289512_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs41289512_C)

rs429358_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs429358_T)

rs4844610_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs4844610_A)

rs6448453_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs6448453_A)

rs6733839_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs6733839_C)

rs6931277_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs6931277_A)

rs73223431_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs73223431_C)

rs7657553_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs7657553_A)

rs7920721_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs7920721_A)

rs7933202_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs7933202_A)

rs8093731_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs8093731_C)

rs9331896_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs9331896_C)

rs9473117_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + rs9473117_A)
```

Extract OR and p-values of the SNPs from these models

``` r
AD_SNP_models_list = c("rs10808026_C",
"rs10933431_G",
"rs11257238_T",
"rs117618017_C",
"rs12539172_T",
"rs12590654_G",
"rs138190086_G",
"rs17125924_A",
"rs190982_G",
"rs2632516_G",
"rs3752246_G",
"rs3851179_T",
"rs3865444_C",
"rs41289512_C",
"rs429358_T",
"rs4844610_A",
"rs6448453_A",
"rs6733839_C",
"rs6931277_A",
"rs73223431_C",
"rs7657553_A",
"rs7920721_A",
"rs7933202_A",
"rs8093731_C",
"rs9331896_C",
"rs9473117_A")
```

For loop

``` r
AD_SNP_df<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(AD_SNP_models_list)){
  
  model_summary = summary(get(AD_SNP_models_list[model]))
  
  snp_name = AD_SNP_models_list[model]
  OR = exp(tail(model_summary$coefficients[,1],n=1))
  upper = exp(tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = exp(tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,OR,upper,lower,p_value)
  #print(add_row)
  AD_SNP_df = rbind(AD_SNP_df,add_row)
}

colnames(AD_SNP_df) <- c("snp_name","OR","upper","lower","p_value")

write.csv(AD_SNP_df, "data_out/SNP_validation_from_simplifiedModels.csv", row.names = F)
```

``` r
rs10808026_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs10808026_C)

rs10933431_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs10933431_G)

rs11257238_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs11257238_T)

rs117618017_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs117618017_C)

rs12539172_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs12539172_T)

rs12590654_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs12590654_G)

rs138190086_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs138190086_G)

rs17125924_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs17125924_A)

rs190982_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs190982_G)

rs2632516_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs2632516_G)

rs3752246_G = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu +  rs3752246_G)

rs3851179_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs3851179_T)

rs3865444_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs3865444_C)

rs41289512_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs41289512_C)

rs429358_T = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu +  rs429358_T)

rs4844610_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs4844610_A)

rs6448453_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs6448453_A)

rs6733839_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age +  edu + rs6733839_C)

rs6931277_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs6931277_A)

rs73223431_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs73223431_C)

rs7657553_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs7657553_A)

rs7920721_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs7920721_A)

rs7933202_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs7933202_A)

rs8093731_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs8093731_C)

rs9331896_C = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs9331896_C)

rs9473117_A = glm(family = "binomial", 
    data = ukb_dt, formula = ad_diag ~ townsend + age + edu + rs9473117_A)

AD_SNP_models_list = c("rs10808026_C",
"rs10933431_G",
"rs11257238_T",
"rs117618017_C",
"rs12539172_T",
"rs12590654_G",
"rs138190086_G",
"rs17125924_A",
"rs190982_G",
"rs2632516_G",
"rs3752246_G",
"rs3851179_T",
"rs3865444_C",
"rs41289512_C",
"rs429358_T",
"rs4844610_A",
"rs6448453_A",
"rs6733839_C",
"rs6931277_A",
"rs73223431_C",
"rs7657553_A",
"rs7920721_A",
"rs7933202_A",
"rs8093731_C",
"rs9331896_C",
"rs9473117_A")

AD_SNP_df_sim<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(AD_SNP_models_list)){
  
  model_summary = summary(get(AD_SNP_models_list[model]))
  
  snp_name = AD_SNP_models_list[model]
  OR = exp(tail(model_summary$coefficients[,1],n=1))
  upper = exp(tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = exp(tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,OR,upper,lower,p_value)
  #print(add_row)
  AD_SNP_df_sim = rbind(AD_SNP_df_sim,add_row)
}

colnames(AD_SNP_df_sim) <- c("snp_name","OR","upper","lower","p_value")

write.csv(AD_SNP_df_sim, "data_out/SNP_validation_from_ageEduModels.csv", row.names = F)
```

Check the snps and how they converge/diverge between the 2 kinds of
models

``` r
subset(AD_SNP_df_sim, p_value< 0.05)$snp_name
```

    ## [1] "rs117618017_C" "rs3865444_C"   "rs6733839_C"   "rs6931277_A"  
    ## [5] "rs7933202_A"   "rs8093731_C"

``` r
subset(AD_SNP_df, p_value< 0.05)$snp_name
```

    ## [1] "rs117618017_C" "rs3865444_C"   "rs6733839_C"   "rs6931277_A"  
    ## [5] "rs73223431_C"  "rs7933202_A"

``` r
AD_SNP_full = rbind(subset(AD_SNP_df_sim, p_value< 0.05),subset(AD_SNP_df, p_value< 0.05))

AD_SNP_full$direction = ifelse(AD_SNP_full$OR > 1,1, -1)
AD_SNP_full$ln_OR = log(as.numeric(AD_SNP_full$OR))
AD_SNP_full$multiplier = AD_SNP_full$direction + AD_SNP_full$ln_OR
```

There is one SNP that is different in both cases. In doubt, I will
include both SNPs together in the PSG. Some SNPs are protective
i.e. OR\<1. The OR of the duplicated SNPs were in the same direction,
so I can simply delete repeated rows.

``` r
psg_snp_dt = subset(AD_SNP_full, select = c(snp_name, multiplier))
psg_snp_dt = aggregate(multiplier ~ snp_name, data=psg_snp_dt, mean)
psg_snp_dt
```

    ##        snp_name multiplier
    ## 1 rs117618017_C  -1.191874
    ## 2   rs3865444_C   1.173805
    ## 3   rs6733839_C  -1.159578
    ## 4   rs6931277_A   1.159326
    ## 5  rs73223431_C  -1.124031
    ## 6   rs7933202_A   1.114174
    ## 7   rs8093731_C  -1.291260

``` r
psg_dt <- subset(ukb_dt, select = c("eid",psg_snp_dt$snp_name))

# check which SNP contribute to an increased vs decreased risk of AD
psg_dt$rs117618017_C = psg_dt$rs117618017_C *-1.191874
psg_dt$rs6733839_C = psg_dt$rs6733839_C*-1.159578
psg_dt$rs8093731_C = psg_dt$rs8093731_C*-1.291260
psg_dt$rs73223431_C = psg_dt$rs73223431_C*-1.124031

psg_dt$rs3865444_C = psg_dt$rs117618017_C *1.173805
psg_dt$rs6931277_A = psg_dt$rs6733839_C*1.159326
psg_dt$rs7933202_A = psg_dt$rs8093731_C*1.114174

psg_dt$ad_psg = rowSums( psg_dt[,2:ncol(psg_dt)] )
psg_dt = subset(psg_dt, select = c(eid,ad_psg))
ukb_dt_psg = merge(ukb_dt, psg_dt, by= "eid", all.x = T)
write.csv(ukb_dt_psg, "data_out/ukb_dt_includingADpsg.csv", row.names = F)
```

AD PSG validation models

``` r
AD_psg_validation_mod = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ sleep_dur + daysleep_sim + insomnia_sim + 
    townsend + age + log_normVitaD + log_normCRP + edu + ad_psg)

summary(AD_psg_validation_mod)
```

Call: glm(formula = ad\_diag \~ sleep\_dur + daysleep\_sim +
insomnia\_sim + townsend + age + log\_normVitaD + log\_normCRP + edu +
ad\_psg, family = “binomial”, data = ukb\_dt\_psg)

Deviance Residuals: Min 1Q Median 3Q Max  
\-0.4691 -0.0698 -0.0465 -0.0290 4.1793

Coefficients: Estimate Std. Error z value Pr(\>|z|)  
(Intercept) -14.237875 0.540246 -26.354 \< 2e-16 *** sleep\_dur 0.130737
0.032952 3.968 7.26e-05 *** daysleep\_sim 0.314471 0.065686 4.787
1.69e-06 *** insomnia\_sim -0.398816 0.055158 -7.230 4.82e-13 ***
townsend 0.035495 0.012589 2.819 0.004810 \*\* age 0.121102 0.005986
20.230 \< 2e-16 *** log\_normVitaD -0.092161 0.082841 -1.113 0.265920  
log\_normCRP -0.139635 0.038378 -3.638 0.000274 *** eduNo certificate
0.713922 0.081482 8.762 \< 2e-16 *** ad\_psg 0.065781 0.015991 4.114
3.89e-05 *** — Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’
’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 9998.1  on 355985  degrees of freedom

Residual deviance: 9212.7 on 355976 degrees of freedom (146518
observations deleted due to missingness) AIC: 9232.7

Number of Fisher Scoring iterations: 10

``` r
stargazer::stargazer(AD_psg_validation_mod,type="html",out = "fig_out/AD_PSG_validation_model_full.html",
          dep.var.labels="AD diagnosis or not",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

AD diagnosis or not

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

sleep\_dur

</td>

<td>

0.131<sup>\*\*\*</sup> (0.033)

</td>

</tr>

<tr>

<td style="text-align:left">

daysleep\_sim

</td>

<td>

0.314<sup>\*\*\*</sup> (0.066)

</td>

</tr>

<tr>

<td style="text-align:left">

insomnia\_sim

</td>

<td>

\-0.399<sup>\*\*\*</sup> (0.055)

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

0.035<sup>\*\*\*</sup> (0.013)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.121<sup>\*\*\*</sup> (0.006)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.092 (0.083)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

\-0.140<sup>\*\*\*</sup> (0.038)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.714<sup>\*\*\*</sup> (0.081)

</td>

</tr>

<tr>

<td style="text-align:left">

ad\_psg

</td>

<td>

0.066<sup>\*\*\*</sup> (0.016)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

\-14.238<sup>\*\*\*</sup> (0.540)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

355,986

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-4,606.346

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

9,232.692

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

``` r
AD_psg_validation_mod_sim = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + ad_psg)

summary(AD_psg_validation_mod_sim)
```

Call: glm(formula = ad\_diag \~ townsend + age + edu + ad\_psg, family =
“binomial”, data = ukb\_dt\_psg)

Deviance Residuals: Min 1Q Median 3Q Max  
\-0.3276 -0.0725 -0.0497 -0.0307 4.1864

Coefficients: Estimate Std. Error z value Pr(\>|z|)  
(Intercept) -12.800129 0.404328 -31.658 \< 2e-16 *** townsend 0.036934
0.011110 3.324 0.000887 *** age 0.121270 0.005415 22.394 \< 2e-16 ***
eduNo certificate 0.664287 0.072605 9.149 \< 2e-16 *** ad\_psg 0.076361
0.014383 5.309 1.1e-07 \*\*\* — Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01
’*’ 0.05 ‘.’ 0.1 ’ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 12240  on 431722  degrees of freedom

Residual deviance: 11429 on 431718 degrees of freedom (70781
observations deleted due to missingness) AIC: 11439

Number of Fisher Scoring iterations: 10

``` r
stargazer::stargazer(AD_psg_validation_mod_sim,type="html",out = "fig_out/AD_PSG_validation_model_simplified.html",
          dep.var.labels="AD diagnosis or not",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

AD diagnosis or not

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

0.037<sup>\*\*\*</sup> (0.011)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.121<sup>\*\*\*</sup> (0.005)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.664<sup>\*\*\*</sup> (0.073)

</td>

</tr>

<tr>

<td style="text-align:left">

ad\_psg

</td>

<td>

0.076<sup>\*\*\*</sup> (0.014)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

\-12.800<sup>\*\*\*</sup> (0.404)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

431,723

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-5,714.726

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

11,439.450

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

## Does mutations in PARP protects against AD?

### PARP and risk of AD

\#\#\#\# Mutations in PARP vs risk of AD

Does mutations in the PARP gene decreases the risk of AD? <br> The PARP
variants are:

``` r
parp_snp_variants = unique(read.csv("data_out/parp_variants_found_in_ukbdt.csv")$raw_var)
parp_snp_variants
```

    ##  [1] "rs1136410_A"   "rs114939615_G" "rs142376976_C" "rs149632681_C"
    ##  [5] "rs1805407_T"   "rs1805410_T"   "rs2230484_G"   "rs3219062_G"  
    ##  [9] "rs3219090_T"   "rs3219123_G"   "rs3219134_T"   "rs3219139_A"  
    ## [13] "rs3219145_T"   "rs78797064_T"  "rs8679_A"

``` r
rs1136410_A = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs1136410_A)

rs1805410_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs1805410_T)

rs3219090_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219090_T)

rs8679_A = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs8679_A)

rs114939615_G = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs114939615_G)

rs142376976_C = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs142376976_C)

rs1805407_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs1805407_T)

rs2230484_G = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs2230484_G)

rs3219062_G = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219062_G)

rs3219134_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219134_T)

rs3219139_A = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219139_A)

rs3219145_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219145_T)

rs78797064_T = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs78797064_T)

rs149632681_C = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs149632681_C)

rs3219123_G = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ townsend + age + edu + rs3219123_G)

PARPsnp_AD_df_sim<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(parp_snp_variants)){
  
  model_summary = summary(get(parp_snp_variants[model]))
  
  snp_name = parp_snp_variants[model]
  OR = exp(tail(model_summary$coefficients[,1],n=1))
  upper = exp(tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = exp(tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,OR,upper,lower,p_value)
  #print(add_row)
  PARPsnp_AD_df_sim = rbind(PARPsnp_AD_df_sim,add_row)
}

colnames(PARPsnp_AD_df_sim) <- c("snp_name","OR","upper","lower","p_value")

write.csv(PARPsnp_AD_df_sim, "data_out/PARPsnp_AD_ageEduModels.csv", row.names = F)
PARPsnp_AD_df_sim
```

``` 
    snp_name                OR                upper                lower
```

1 rs1136410\_A 1.09696483675631 1.17173153423148 1.02696890706201 2
rs114939615\_G 1.00829753213553 1.10428751408615 0.920651461093379 3
rs142376976\_C 75313.7454450715 1.10689994728687e+71
5.12436581722497e-62 4 rs149632681\_C 7136.55532606594
7.68740359204607e+52 6.62517862008662e-46 5 rs1805407\_T
0.930812285476122 0.988648486463734 0.876359517721331 6 rs1805410\_T
1.0337605211495 1.10148330573153 0.970201554146613 7 rs2230484\_G
0.802773013444987 1.05156781673046 0.612841607419343 8 rs3219062\_G
1.3031094868013 2.1523189023827 0.788960377902962 9 rs3219090\_T
1.0090214665607 1.05950898064652 0.960939773591202 10 rs3219123\_G
1.0361897729952 1.14842044020245 0.934926972799766 11 rs3219134\_T
1.4167790571309 1.65678160824691 1.21154344467203 12 rs3219139\_A
1.178805373664 1.36112825379596 1.02090460991006 13 rs3219145\_T
153486.900474013 2.04691551544645e+72 1.15091357896036e-62 14
rs78797064\_T 1.29112595085551 1.56799821180841 1.06314293499732 15
rs8679\_A 1.02565165438842 1.0845282577232 0.969971329615824 p\_value 1
0.160437549689554 2 0.927597221058871 3 0.941244900652426 4
0.937358078545585 5 0.234287706057541 6 0.60079444946768 7
0.41579059785894 8 0.597766480138261 9 0.854056879063351 10
0.72957184875546 11 0.0259982323999775 12 0.252680976806243 13
0.938416810606552 14 0.188458456749975 15 0.649992831746984

``` r
subset(PARPsnp_AD_df_sim, p_value < 0.05)
```

    ##       snp_name              OR            upper            lower
    ## 11 rs3219134_T 1.4167790571309 1.65678160824691 1.21154344467203
    ##               p_value
    ## 11 0.0259982323999775

Only rs3219134 is significant here. This is an uncharacterised SNP:
<https://www.ncbi.nlm.nih.gov/snp/rs3219134>. <br> Following the method
described here
(<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3805565/>), I will have
explore whether Human Splice Finder can shed light whether this intron
(rs3219134\_T) has any effect on PARP1.

#### Mutations in PARP vs risk of AD in genetically susceptible people

``` r
summary(ukb_dt_psg$ad_psg)
```

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
    ##  -17.90  -15.65  -14.27  -14.34  -12.89   -2.73   69757

``` r
ukb_dt_psg_upper = subset(ukb_dt_psg, ad_psg>mean(na.omit(ukb_dt_psg$ad_psg)))
```

``` r
rs1136410_A = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs1136410_A)

rs1805410_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs1805410_T)

rs3219090_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219090_T)

rs8679_A = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs8679_A)

rs114939615_G = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs114939615_G)

rs142376976_C = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs142376976_C)

rs1805407_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs1805407_T)

rs2230484_G = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs2230484_G)

rs3219062_G = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219062_G)

rs3219134_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219134_T)

rs3219139_A = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219139_A)

rs3219145_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219145_T)

rs78797064_T = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs78797064_T)

rs149632681_C = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs149632681_C)

rs3219123_G = glm(family = "binomial", 
    data = ukb_dt_psg_upper, formula = ad_diag ~ townsend + age + edu + rs3219123_G)

PARPsnp_AD_df_sim_upper<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(parp_snp_variants)){
  
  model_summary = summary(get(parp_snp_variants[model]))
  
  snp_name = parp_snp_variants[model]
  OR = exp(tail(model_summary$coefficients[,1],n=1))
  upper = exp(tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = exp(tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,OR,upper,lower,p_value)
  #print(add_row)
  PARPsnp_AD_df_sim_upper = rbind(PARPsnp_AD_df_sim_upper,add_row)
}

colnames(PARPsnp_AD_df_sim_upper) <- c("snp_name","OR","upper","lower","p_value")

write.csv(PARPsnp_AD_df_sim_upper, "data_out/PARPsnp_AD_ageEduModels_lowerADpsg.csv", row.names = F)
PARPsnp_AD_df_sim_upper
```

    ##         snp_name                OR                upper                lower
    ## 1    rs1136410_A  1.17324670593688     1.28556047069192     1.07074530088099
    ## 2  rs114939615_G 0.950890025806965     1.07278754409225    0.842843344107117
    ## 3  rs142376976_C  29695.7045858177 4.95640962590391e+63 1.77918077279039e-55
    ## 4  rs149632681_C  6716.20215791259 4.70140462417484e+70 9.59444570969384e-64
    ## 5    rs1805407_T 0.926425167898387     1.00586939783623    0.853255495755018
    ## 6    rs1805410_T  1.03167392384925     1.12455777223996    0.946461899445574
    ## 7    rs2230484_G 0.868596561070837     1.27219404882635    0.593038449283822
    ## 8    rs3219062_G  2.93437043404661      7.9897023926457     1.07770345139922
    ## 9    rs3219090_T 0.981556374663687     1.04918625378067    0.918285874572968
    ## 10   rs3219123_G 0.971259240991101     1.11219793686533    0.848180419997336
    ## 11   rs3219134_T  2.21931158748444     2.87967693709702     1.71038072323068
    ## 12   rs3219139_A  1.15476702386715     1.40430088652413    0.949573479734516
    ## 13   rs3219145_T  180287.821841741 8.11963660548947e+93 4.00309771036615e-84
    ## 14  rs78797064_T  1.09238322034497      1.3957306079601    0.854965201225538
    ## 15      rs8679_A  1.05654105540803     1.14030429046532    0.978930809167796
    ##               p_value
    ## 1  0.0805154670753849
    ## 2   0.676317947729258
    ## 3   0.939798131412634
    ## 4   0.954343170545274
    ## 5    0.35295692161756
    ## 6   0.717563204441951
    ## 7   0.712012659979762
    ## 8   0.282505353826077
    ## 9   0.779946935262134
    ## 10  0.829598425455585
    ## 11   0.00220982592767
    ## 12  0.462020494281608
    ## 13  0.952723855224012
    ## 14  0.718415384739953
    ## 15  0.470974708379555

Significance:

``` r
subset(PARPsnp_AD_df_sim_upper, p_value < 0.05)
```

    ##       snp_name               OR            upper            lower
    ## 11 rs3219134_T 2.21931158748444 2.87967693709702 1.71038072323068
    ##             p_value
    ## 11 0.00220982592767

This confirms the finding above, in the total cohort.

#### Mutations in PARP vs risk of AD in low risk people

``` r
ukb_dt_psg_lower = subset(ukb_dt_psg, ad_psg < mean(na.omit(ukb_dt_psg$ad_psg)))

rs1136410_A = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs1136410_A)

rs1805410_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs1805410_T)

rs3219090_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219090_T)

rs8679_A = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs8679_A)

rs114939615_G = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs114939615_G)

rs142376976_C = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs142376976_C)

rs1805407_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs1805407_T)

rs2230484_G = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs2230484_G)

rs3219062_G = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219062_G)

rs3219134_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219134_T)

rs3219139_A = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219139_A)

rs3219145_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219145_T)

rs78797064_T = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs78797064_T)

rs149632681_C = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs149632681_C)

rs3219123_G = glm(family = "binomial", 
    data = ukb_dt_psg_lower, formula = ad_diag ~ townsend + age + edu + rs3219123_G)

ukb_dt_psg_lower<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(parp_snp_variants)){
  
  model_summary = summary(get(parp_snp_variants[model]))
  
  snp_name = parp_snp_variants[model]
  OR = exp(tail(model_summary$coefficients[,1],n=1))
  upper = exp(tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = exp(tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,OR,upper,lower,p_value)
  #print(add_row)
  ukb_dt_psg_lower = rbind(ukb_dt_psg_lower,add_row)
}

colnames(ukb_dt_psg_lower) <- c("snp_name","OR","upper","lower","p_value")

write.csv(ukb_dt_psg_lower, "data_out/PARPsnp_AD_ageEduModels_lowerADpsg.csv", row.names = F)
ukb_dt_psg_lower
```

    ##         snp_name                OR                 upper                 lower
    ## 1    rs1136410_A 0.977140465001381      1.08889792133497     0.876853072850521
    ## 2  rs114939615_G  1.20437620172198      1.42393653970683      1.01867042162771
    ## 3  rs142376976_C  66511.4680729256 4.17414562226888e+106  1.05980379831864e-97
    ## 4  rs149632681_C  7089.47639470839  1.92948375742129e+82  2.60487684116604e-75
    ## 5    rs1805407_T 0.906719361991737      1.00315671336641     0.819552907792196
    ## 6    rs1805410_T  1.07066657847741      1.19422179338553     0.959894492478473
    ## 7    rs2230484_G 0.551265004850426     0.808802894134304     0.375731971011317
    ## 8    rs3219062_G 0.852868269532947      1.73611089946772     0.418973399337067
    ## 9    rs3219090_T  1.08347671838586      1.17618864686843     0.998072717679874
    ## 10   rs3219123_G  1.31159183648905       1.5964156881919      1.07758471572847
    ## 11   rs3219134_T 0.748232623962344      0.91550178691901     0.611524813562272
    ## 12   rs3219139_A  1.40772210934721      1.82968424795285      1.08307296155726
    ## 13   rs3219145_T  121437.734863027 3.64639280070231e+110 4.04430467442308e-101
    ## 14  rs78797064_T  3.09665755207921      5.11610629842133      1.87433322052127
    ## 15      rs8679_A 0.990063910667733      1.08810294007333     0.900858283813314
    ##               p_value
    ## 1   0.830902825737794
    ## 2   0.266800208071477
    ## 3     0.9622125384271
    ## 4   0.960845047751491
    ## 5   0.332636255615655
    ## 6   0.531832281434684
    ## 7    0.12029030099253
    ## 8   0.822832294959797
    ## 9   0.328814897695257
    ## 10  0.167516468352074
    ## 11  0.150556740380379
    ## 12  0.192100323491882
    ## 13  0.961554298730322
    ## 14 0.0243649842308073
    ## 15  0.915774793650701

Significance

``` r
subset(ukb_dt_psg_lower, p_value < 0.05)
```

    ##        snp_name               OR            upper            lower
    ## 14 rs78797064_T 3.09665755207921 5.11610629842133 1.87433322052127
    ##               p_value
    ## 14 0.0243649842308073

Here, there seem to be a new SNP that emerged: rs78797064. It is another
intron, so I can process that SNP at the same time Human Splice Finder.

### PARP and sleep in AD patients

#### Create sleepiness score

sleep\_dur 0.130737 0.032952 3.968 7.26e-05 *** daysleep\_sim 0.314471
0.065686 4.787 1.69e-06 *** insomnia\_sim -0.398816

``` r
ukb_dt_psg$sleepiness = ukb_dt_psg$sleep_dur+ukb_dt_psg$daysleep_sim-ukb_dt_psg$insomnia_sim
```

Validation

``` r
AD_psg_validation_sleepiness = glm(family = "binomial", 
    data = ukb_dt_psg, formula = ad_diag ~ sleepiness + 
    townsend + age + log_normVitaD + log_normCRP + edu + ad_psg)

summary(AD_psg_validation_sleepiness)
```

Call: glm(formula = ad\_diag \~ sleepiness + townsend + age +
log\_normVitaD + log\_normCRP + edu + ad\_psg, family = “binomial”, data
= ukb\_dt\_psg)

Deviance Residuals: Min 1Q Median 3Q Max  
\-0.4439 -0.0702 -0.0469 -0.0292 4.1700

Coefficients: Estimate Std. Error z value Pr(\>|z|)  
(Intercept) -14.989911 0.506686 -29.584 \< 2e-16 *** sleepiness 0.218673
0.023121 9.458 \< 2e-16 *** townsend 0.036017 0.012567 2.866 0.004158
\*\* age 0.120265 0.005975 20.127 \< 2e-16 *** log\_normVitaD -0.096049
0.082756 -1.161 0.245793  
log\_normCRP -0.146155 0.038361 -3.810 0.000139 *** eduNo certificate
0.700334 0.081271 8.617 \< 2e-16 *** ad\_psg 0.066031 0.015990 4.129
3.64e-05 *** — Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’
’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 9998.1  on 355985  degrees of freedom

Residual deviance: 9229.0 on 355978 degrees of freedom (146518
observations deleted due to missingness) AIC: 9245

Number of Fisher Scoring iterations: 10

``` r
stargazer::stargazer(AD_psg_validation_sleepiness,type="html",out = "fig_out/AD_PSG_validation_sleepiness_score.html",
          dep.var.labels="AD diagnosis or not",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

AD diagnosis or not

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

sleepiness

</td>

<td>

0.219<sup>\*\*\*</sup> (0.023)

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

0.036<sup>\*\*\*</sup> (0.013)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.120<sup>\*\*\*</sup> (0.006)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.096 (0.083)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

\-0.146<sup>\*\*\*</sup> (0.038)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.700<sup>\*\*\*</sup> (0.081)

</td>

</tr>

<tr>

<td style="text-align:left">

ad\_psg

</td>

<td>

0.066<sup>\*\*\*</sup> (0.016)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

\-14.990<sup>\*\*\*</sup> (0.507)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

355,986

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-4,614.516

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

9,245.031

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

#### Model PARP and sleep in AD patients

``` r
ukb_dt_psgAD = subset(ukb_dt_psg, ad_diag == TRUE)
nrow(ukb_dt_psgAD)
```

    ## [1] 1005

##### Determine the target variables

``` r
library(MASS)
sleepAD_validation_model_dt = subset(ukb_dt_psg, ad_diag == TRUE,select = c(sleepiness,townsend, ethnicity_sim, whr, sex, age, 
                             log_normVitaD, log_normCRP, edu, highBP))

sleepAD_validation_model= glm.nb(data = na.omit(sleepAD_validation_model_dt), sleepiness ~ townsend+ethnicity_sim+whr + sex + age+
                             log_normVitaD+log_normCRP+edu+highBP)
```

    ## Warning in theta.ml(Y, mu, sum(w), w, limit = control$maxit, trace =
    ## control$trace > : iteration limit reached
    
    ## Warning in theta.ml(Y, mu, sum(w), w, limit = control$maxit, trace =
    ## control$trace > : iteration limit reached

``` r
summary(sleepAD_validation_model)
```

Call: glm.nb(formula = sleepiness \~ townsend + ethnicity\_sim + whr +
sex + age + log\_normVitaD + log\_normCRP + edu + highBP, data =
na.omit(sleepAD\_validation\_model\_dt), init.theta = 313184.7171, link
= log)

Deviance Residuals: Min 1Q Median 3Q Max  
\-2.82498 -0.39406 0.00116 0.38425 1.84797

Coefficients: Estimate Std. Error z value Pr(\>|z|)  
(Intercept) 1.601263 0.288811 5.544 2.95e-08 \*\*\* townsend -0.006338
0.004593 -1.380 0.168  
ethnicity\_simMinority 0.006422 0.049020 0.131 0.896  
whr 0.180867 0.214173 0.844 0.398  
sexMale 0.027236 0.037259 0.731 0.465  
age 0.002349 0.003275 0.717 0.473  
log\_normVitaD -0.009973 0.029149 -0.342 0.732  
log\_normCRP 0.001175 0.012939 0.091 0.928  
eduNo certificate 0.002298 0.029885 0.077 0.939  
highBP 0.007259 0.035293 0.206 0.837  
— Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’ ’ 1

(Dispersion parameter for Negative Binomial(313184.7) family taken to be
1)

    Null deviance: 321.83  on 745  degrees of freedom

Residual deviance: 315.51 on 736 degrees of freedom AIC: 3150.3

Number of Fisher Scoring iterations: 1

``` 
          Theta:  313185 
      Std. Err.:  1716659 
```

Warning while fitting theta: iteration limit reached

2 x log-likelihood: -3128.277

``` r
stargazer::stargazer(sleepAD_validation_model,type="html",out = "fig_out/sleep_inADpatients_validation_model_NB.html",
          dep.var.labels="Sleepiness score",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

Sleepiness score

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

\-0.006 (0.005)

</td>

</tr>

<tr>

<td style="text-align:left">

ethnicity\_simMinority

</td>

<td>

0.006 (0.049)

</td>

</tr>

<tr>

<td style="text-align:left">

whr

</td>

<td>

0.181 (0.214)

</td>

</tr>

<tr>

<td style="text-align:left">

sexMale

</td>

<td>

0.027 (0.037)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.002 (0.003)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.010 (0.029)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

0.001 (0.013)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.002 (0.030)

</td>

</tr>

<tr>

<td style="text-align:left">

highBP

</td>

<td>

0.007 (0.035)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

1.601<sup>\*\*\*</sup> (0.289)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

746

</td>

</tr>

<tr>

<td style="text-align:left">

Log Likelihood

</td>

<td>

\-1,565.139

</td>

</tr>

<tr>

<td style="text-align:left">

theta

</td>

<td>

313,184.700 (1,716,659.000)

</td>

</tr>

<tr>

<td style="text-align:left">

Akaike Inf. Crit.

</td>

<td>

3,150.277

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

Try with logistics instead

``` r
sleepAD_validation_model_dt = subset(ukb_dt_psg, ad_diag == TRUE,select = c(sleepiness,townsend, ethnicity_sim, whr, sex, age, 
                             log_normVitaD, log_normCRP, edu, highBP))

sleepAD_validation_model= lm(data = na.omit(sleepAD_validation_model_dt), sleepiness ~ townsend+ethnicity_sim+whr + sex + age+
                             log_normVitaD+log_normCRP+edu+highBP)
summary(sleepAD_validation_model)
```

Call: lm(formula = sleepiness \~ townsend + ethnicity\_sim + whr + sex +
age + log\_normVitaD + log\_normCRP + edu + highBP, data =
na.omit(sleepAD\_validation\_model\_dt))

Residuals: Min 1Q Median 3Q Max -5.9292 -1.0223 -0.0004 1.0345 5.3181

Coefficients: Estimate Std. Error t value Pr(\>|t|)  
(Intercept) 4.61603 1.28345 3.597 0.000344 \*\** townsend -0.04374
0.02034 -2.151 0.031840 *  
ethnicity\_simMinority 0.04413 0.21869 0.202 0.840145  
whr 1.25567 0.95617 1.313 0.189513  
sexMale 0.18929 0.16627 1.138 0.255324  
age 0.01625 0.01453 1.118 0.263912  
log\_normVitaD -0.06920 0.13017 -0.532 0.595159  
log\_normCRP 0.00837 0.05778 0.145 0.884860  
eduNo certificate 0.01615 0.13342 0.121 0.903697  
highBP 0.05067 0.15828 0.320 0.748957  
— Signif. codes: 0 ‘***’ 0.001 ’**’ 0.01 ’*’ 0.05 ‘.’ 0.1 ’ ’ 1

Residual standard error: 1.692 on 736 degrees of freedom Multiple
R-squared: 0.02039, Adjusted R-squared: 0.008414 F-statistic: 1.702 on 9
and 736 DF, p-value: 0.08466

``` r
stargazer::stargazer(sleepAD_validation_model,type="html",out = "fig_out/sleep_inADpatients_validation_model_LM.html",
          dep.var.labels="Sleepiness score",
          single.row=TRUE)
```

<table style="text-align:center">

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

<em>Dependent variable:</em>

</td>

</tr>

<tr>

<td>

</td>

<td colspan="1" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

</td>

<td>

Sleepiness score

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

townsend

</td>

<td>

\-0.044<sup>\*\*</sup> (0.020)

</td>

</tr>

<tr>

<td style="text-align:left">

ethnicity\_simMinority

</td>

<td>

0.044 (0.219)

</td>

</tr>

<tr>

<td style="text-align:left">

whr

</td>

<td>

1.256 (0.956)

</td>

</tr>

<tr>

<td style="text-align:left">

sexMale

</td>

<td>

0.189 (0.166)

</td>

</tr>

<tr>

<td style="text-align:left">

age

</td>

<td>

0.016 (0.015)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normVitaD

</td>

<td>

\-0.069 (0.130)

</td>

</tr>

<tr>

<td style="text-align:left">

log\_normCRP

</td>

<td>

0.008 (0.058)

</td>

</tr>

<tr>

<td style="text-align:left">

eduNo certificate

</td>

<td>

0.016 (0.133)

</td>

</tr>

<tr>

<td style="text-align:left">

highBP

</td>

<td>

0.051 (0.158)

</td>

</tr>

<tr>

<td style="text-align:left">

Constant

</td>

<td>

4.616<sup>\*\*\*</sup> (1.283)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

Observations

</td>

<td>

746

</td>

</tr>

<tr>

<td style="text-align:left">

R<sup>2</sup>

</td>

<td>

0.020

</td>

</tr>

<tr>

<td style="text-align:left">

Adjusted R<sup>2</sup>

</td>

<td>

0.008

</td>

</tr>

<tr>

<td style="text-align:left">

Residual Std. Error

</td>

<td>

1.692 (df = 736)

</td>

</tr>

<tr>

<td style="text-align:left">

F Statistic

</td>

<td>

1.702<sup>\*</sup> (df = 9; 736)

</td>

</tr>

<tr>

<td colspan="2" style="border-bottom: 1px solid black">

</td>

</tr>

<tr>

<td style="text-align:left">

<em>Note:</em>

</td>

<td style="text-align:right">

<sup>*</sup>p\<0.1; <sup>**</sup>p\<0.05; <sup>***</sup>p\<0.01

</td>

</tr>

</table>

Reduce the model with stepAIC

``` r
stepAIC(sleepAD_validation_model)
```

    ## Start:  AIC=794.28
    ## sleepiness ~ townsend + ethnicity_sim + whr + sex + age + log_normVitaD + 
    ##     log_normCRP + edu + highBP
    ## 
    ##                 Df Sum of Sq    RSS    AIC
    ## - edu            1    0.0419 2106.2 792.29
    ## - log_normCRP    1    0.0601 2106.2 792.30
    ## - ethnicity_sim  1    0.1165 2106.3 792.32
    ## - highBP         1    0.2933 2106.5 792.38
    ## - log_normVitaD  1    0.8087 2107.0 792.56
    ## - age            1    3.5771 2109.8 793.54
    ## - sex            1    3.7086 2109.9 793.59
    ## - whr            1    4.9352 2111.1 794.02
    ## <none>                       2106.2 794.28
    ## - townsend       1   13.2343 2119.4 796.95
    ## 
    ## Step:  AIC=792.29
    ## sleepiness ~ townsend + ethnicity_sim + whr + sex + age + log_normVitaD + 
    ##     log_normCRP + highBP
    ## 
    ##                 Df Sum of Sq    RSS    AIC
    ## - log_normCRP    1    0.0664 2106.3 790.32
    ## - ethnicity_sim  1    0.1025 2106.3 790.33
    ## - highBP         1    0.3063 2106.5 790.40
    ## - log_normVitaD  1    0.8198 2107.0 790.58
    ## - sex            1    3.6762 2109.9 791.59
    ## - age            1    3.6985 2109.9 791.60
    ## - whr            1    4.9806 2111.2 792.05
    ## <none>                       2106.2 792.29
    ## - townsend       1   13.5626 2119.8 795.08
    ## 
    ## Step:  AIC=790.32
    ## sleepiness ~ townsend + ethnicity_sim + whr + sex + age + log_normVitaD + 
    ##     highBP
    ## 
    ##                 Df Sum of Sq    RSS    AIC
    ## - ethnicity_sim  1    0.0941 2106.4 788.35
    ## - highBP         1    0.3218 2106.6 788.43
    ## - log_normVitaD  1    0.8185 2107.1 788.61
    ## - sex            1    3.6788 2110.0 789.62
    ## - age            1    3.7275 2110.0 789.63
    ## <none>                       2106.3 790.32
    ## - whr            1    5.6813 2112.0 790.32
    ## - townsend       1   13.4966 2119.8 793.08
    ## 
    ## Step:  AIC=788.35
    ## sleepiness ~ townsend + whr + sex + age + log_normVitaD + highBP
    ## 
    ##                 Df Sum of Sq    RSS    AIC
    ## - highBP         1    0.3216 2106.7 786.46
    ## - log_normVitaD  1    0.8506 2107.2 786.65
    ## - age            1    3.7061 2110.1 787.66
    ## - sex            1    3.7207 2110.1 787.67
    ## <none>                       2106.4 788.35
    ## - whr            1    5.6789 2112.1 788.36
    ## - townsend       1   13.4569 2119.8 791.10
    ## 
    ## Step:  AIC=786.46
    ## sleepiness ~ townsend + whr + sex + age + log_normVitaD
    ## 
    ##                 Df Sum of Sq    RSS    AIC
    ## - log_normVitaD  1    0.9137 2107.6 784.79
    ## - sex            1    3.7218 2110.4 785.78
    ## - age            1    3.8325 2110.5 785.82
    ## <none>                       2106.7 786.46
    ## - whr            1    5.9220 2112.6 786.56
    ## - townsend       1   13.4412 2120.1 789.21
    ## 
    ## Step:  AIC=784.79
    ## sleepiness ~ townsend + whr + sex + age
    ## 
    ##            Df Sum of Sq    RSS    AIC
    ## - sex       1    3.3192 2110.9 783.96
    ## - age       1    3.5621 2111.2 784.05
    ## <none>                  2107.6 784.79
    ## - whr       1    6.6599 2114.3 785.14
    ## - townsend  1   12.6669 2120.3 787.26
    ## 
    ## Step:  AIC=783.96
    ## sleepiness ~ townsend + whr + age
    ## 
    ##            Df Sum of Sq    RSS    AIC
    ## - age       1    3.7349 2114.7 783.28
    ## <none>                  2110.9 783.96
    ## - townsend  1   13.9606 2124.9 786.88
    ## - whr       1   22.4170 2133.3 789.84
    ## 
    ## Step:  AIC=783.28
    ## sleepiness ~ townsend + whr
    ## 
    ##            Df Sum of Sq    RSS    AIC
    ## <none>                  2114.7 783.28
    ## - townsend  1    14.109 2128.8 786.24
    ## - whr       1    23.419 2138.1 789.49

    ## 
    ## Call:
    ## lm(formula = sleepiness ~ townsend + whr, data = na.omit(sleepAD_validation_model_dt))
    ## 
    ## Coefficients:
    ## (Intercept)     townsend          whr  
    ##     5.09888     -0.04272      2.04067

``` r
rs1136410_A = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1136410_A)

rs1805410_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1805410_T)

rs3219090_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219090_T)

rs8679_A = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs8679_A)

rs114939615_G = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs114939615_G)

rs142376976_C = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs142376976_C)

rs1805407_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1805407_T)

rs2230484_G = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs2230484_G)

rs3219062_G = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219062_G)

rs3219134_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219134_T)

rs3219139_A = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219139_A)

rs3219145_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219145_T)

rs78797064_T = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs78797064_T)

rs149632681_C = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs149632681_C)

rs3219123_G = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219123_G)

PARPsnp_sleep_ADpatient<-data.frame(
  snp_name=character(),Beta=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(parp_snp_variants)){
  
  model_summary = summary(get(parp_snp_variants[model]))
  
  snp_name = parp_snp_variants[model]
  Beta = (tail(model_summary$coefficients[,1],n=1))
  upper = (tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = (tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,Beta,upper,lower,p_value)
  #print(add_row)
  PARPsnp_sleep_ADpatient = rbind(PARPsnp_sleep_ADpatient,add_row)
}

colnames(PARPsnp_sleep_ADpatient) <- c("snp_name","Beta","upper","lower","p_value")

write.csv(PARPsnp_sleep_ADpatient, "data_out/PARPsnp_andSleep_in_ADpatient.csv", row.names = F)
PARPsnp_sleep_ADpatient
```

    ##         snp_name                 Beta               upper                lower
    ## 1    rs1136410_A   0.0599940696957464   0.176723553507193  -0.0567354141157001
    ## 2  rs114939615_G    0.195873767774447   0.358605317389098   0.0331422181597957
    ## 3  rs142376976_C     0.85998155811167    1.72231911576947 -0.00235599954613219
    ## 4  rs149632681_C    0.824108677210497    1.69477819593457  -0.0465608415135762
    ## 5    rs1805407_T   -0.177468498563957 -0.0707257204465716   -0.284211276681343
    ## 6    rs1805410_T -0.00125167572197677   0.112373325300812   -0.114876676744766
    ## 7    rs2230484_G   -0.983147367360503  -0.505312665523896    -1.46098206919711
    ## 8    rs3219062_G     0.43796686835505    1.32517496096072    -0.44924122425062
    ## 9    rs3219090_T   0.0747176610167552   0.164622877720205  -0.0151875556866951
    ## 10   rs3219123_G    0.126683145201688   0.312012287454888  -0.0586459970515123
    ## 11   rs3219134_T   -0.159415678984522   0.113471071705716    -0.43230242967476
    ## 12   rs3219139_A   -0.181957366766642  0.0735766480758308   -0.437491381609115
    ## 13   rs3219145_T    0.907666091915686    1.77260053593372   0.0427316478976547
    ## 14  rs78797064_T   -0.571130961246682  -0.219297790665039   -0.922964131828325
    ## 15      rs8679_A   0.0596065018981043   0.158355379685166  -0.0391423758889578
    ##               p_value
    ## 1   0.607404803820085
    ## 2   0.229030230594198
    ## 3   0.318896715395823
    ## 4   0.344132362197656
    ## 5  0.0967500616911074
    ## 6   0.991213198894488
    ## 7  0.0399199300815302
    ## 8   0.621674046006409
    ## 9   0.406149825120129
    ## 10  0.494427052194957
    ## 11   0.55924133247218
    ## 12  0.476617470938042
    ## 13  0.294267877337084
    ## 14  0.104868498758257
    ## 15  0.546248731552028

``` r
subset(PARPsnp_sleep_ADpatient, p_value < 0.05)
```

    ##      snp_name               Beta              upper             lower
    ## 7 rs2230484_G -0.983147367360503 -0.505312665523896 -1.46098206919711
    ##              p_value
    ## 7 0.0399199300815302

Interestingly, this is an exon sequence in PARP1:
<https://www.ncbi.nlm.nih.gov/variation/view/?q=rs2230484>. <br> This
indicates that having the G (major) allele decreases the risk of
sleepiness. The minor allele (A/T) is therefore protective. This may
lead to a missense mutation
(<https://www.ncbi.nlm.nih.gov/clinvar/variation/779066/>).

Confirmation that G is the major allele

``` r
summary(factor(ukb_dt_psgAD$rs2230484_G))
```

    ##    1    2 NA's 
    ##   14  938   53

I will investigate this further based on this study using SNAP

#### Quick exploration of the effect of sleep on sleep in the whole population

``` r
rs1136410_A = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1136410_A)

rs1805410_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1805410_T)

rs3219090_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219090_T)

rs8679_A = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs8679_A)

rs114939615_G = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs114939615_G)

rs142376976_C = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs142376976_C)

rs1805407_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs1805407_T)

rs2230484_G = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs2230484_G)

rs3219062_G = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219062_G)

rs3219134_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219134_T)

rs3219139_A = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219139_A)

rs3219145_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219145_T)

rs78797064_T = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs78797064_T)

rs149632681_C = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs149632681_C)

rs3219123_G = lm(
    data = ukb_dt_psg, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs3219123_G)

PARPsnp_sleep_wholeUKB<-data.frame(
  snp_name=character(),OR=double(),upper=double(),lower=double(),p_value=double())

for (model in 1:length(parp_snp_variants)){
  
  model_summary = summary(get(parp_snp_variants[model]))
  
  snp_name = parp_snp_variants[model]
  Beta = (tail(model_summary$coefficients[,1],n=1))
  upper = (tail(model_summary$coefficients[,1],n=1) + tail(model_summary$coefficients[,2],n=1))
  lower = (tail(model_summary$coefficients[,1],n=1) - tail(model_summary$coefficients[,2],n=1))
  p_value = tail(model_summary$coefficients[,4],n=1)
  
  add_row = c(snp_name,Beta,upper,lower,p_value)
  #print(add_row)
  PARPsnp_sleep_wholeUKB = rbind(PARPsnp_sleep_wholeUKB,add_row)
}

colnames(PARPsnp_sleep_wholeUKB) <- c("snp_name","Beta","upper","lower","p_value")

write.csv(PARPsnp_sleep_wholeUKB, "data_out/PARPsnp_sleep_wholeUKB.csv", row.names = F)
PARPsnp_sleep_wholeUKB
```

    ##         snp_name                  Beta                upper
    ## 1    rs1136410_A   0.00641571629954067   0.0107218299245974
    ## 2  rs114939615_G   -0.0038830905695294  0.00225560856888076
    ## 3  rs142376976_C    -0.173602079994392   -0.111445848372614
    ## 4  rs149632681_C     0.231735159913595    0.361349851235299
    ## 5    rs1805407_T  0.000578712578511582  0.00471699510105328
    ## 6    rs1805410_T -0.000937846926528944  0.00328948076299841
    ## 7    rs2230484_G   0.00259688467589121   0.0230474439060728
    ## 8    rs3219062_G    0.0152524930454318   0.0448257075192854
    ## 9    rs3219090_T  -0.00268900288489427 0.000597854358195563
    ## 10   rs3219123_G  -0.00458069716173141  0.00224950887704686
    ## 11   rs3219134_T   0.00296292809851332   0.0120569538326732
    ## 12   rs3219139_A   -0.0143815873040387 -0.00546691231771907
    ## 13   rs3219145_T      -0.1458967918329   -0.106588333635613
    ## 14  rs78797064_T    0.0285976629380344   0.0402561627984238
    ## 15      rs8679_A   0.00306033005188826  0.00678996979137718
    ##                    lower              p_value
    ## 1    0.00210960267448392    0.136248891805922
    ## 2    -0.0100217897079396    0.527021844125643
    ## 3      -0.23575831161617  0.00522244725169214
    ## 4      0.102120468591891   0.0737964480376833
    ## 5   -0.00355956994403011    0.888783576173286
    ## 6    -0.0051651746160563    0.824428119822768
    ## 7    -0.0178536745542903    0.898953469008557
    ## 8    -0.0143207214284217    0.606026722143802
    ## 9    -0.0059758601279841    0.413296157684536
    ## 10   -0.0114109032005097    0.502442027656176
    ## 11  -0.00613109763564658    0.744567957895368
    ## 12   -0.0232962622903583    0.106691203310824
    ## 13    -0.185205250030187 0.000205986521808963
    ## 14    0.0169391630776451   0.0141695399169422
    ## 15 -0.000669309687600657    0.411906995064211

rs3219134\_T

``` r
subset(PARPsnp_sleep_wholeUKB, p_value < 0.05)
```

    ##         snp_name               Beta              upper              lower
    ## 3  rs142376976_C -0.173602079994392 -0.111445848372614  -0.23575831161617
    ## 13   rs3219145_T   -0.1458967918329 -0.106588333635613 -0.185205250030187
    ## 14  rs78797064_T 0.0285976629380344 0.0402561627984238 0.0169391630776451
    ##                 p_value
    ## 3   0.00522244725169214
    ## 13 0.000205986521808963
    ## 14   0.0141695399169422

Interestingly, rs78797064\_T is also associated with a higher risk of AD
in patients with low genetic risk. The importance of intronic SNPs are
explained here: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3500160/>.
I will therefore explore rs78797064\_T further.

### Investigate whether there are any PARP1-related genes in the SNPs identified in the EBI GWAS dataset

There is no intersection…

``` r
AD_ebi_snp_dt = read.csv("data/efotraits_EFO_0000249-associations-2020-12-5.csv")
parp_snp_dt = read.csv("data/PARP_snp_result.txt", sep = "\t")
merge(AD_ebi_snp_dt,parp_snp_dt,
      by.x = "Variant.and.risk.allele",by.y = "snp_id")
```

    ##  [1] Variant.and.risk.allele P.value                 P.value.annotation     
    ##  [4] RAF                     OR                      Beta                   
    ##  [7] CI                      Mapped.gene             Reported.trait         
    ## [10] Trait.s.                Study.accession         Location               
    ## [13] X.chr                   pos                     variation              
    ## [16] variant_type            clinical_significance   validation_status      
    ## [19] function_class          gene                    frequency              
    ## <0 rows> (or 0-length row.names)

### Making the figures for the PARP data

#### Descriptive data

``` r
full_dt = read.csv('data_out/ukb_dt_includingADpsg.csv')

length(na.omit(full_dt$ad_psg))
```

    ## [1] 432747

``` r
ADpsg_dt = subset(full_dt, !is.na(ad_psg))

length(ADpsg_dt$ad_diag[ADpsg_dt$ad_diag == TRUE])
```

    ## [1] 847

``` r
length(ADpsg_dt$ad_diag[ADpsg_dt$ad_diag == FALSE])
```

    ## [1] 431900

``` r
ADpsg_dt$sleepiness = ADpsg_dt$sleep_dur+ADpsg_dt$daysleep_sim-ADpsg_dt$insomnia_sim
ADpsg_dt$date_assessed <- NA

library(arsenal)
ukb_descript_stats <- tableby(ad_diag ~ ., data =ADpsg_dt[,2:ncol(ADpsg_dt)])
write2word(ukb_descript_stats, "ukb_descriptStats.doc",
           keep.md = TRUE,
           quiet = TRUE, # passed to rmarkdown::render
           title = "Descriptive statistics of the UK Biobank data") # passed to summary.tableby
```

#### Sleepiness model

``` r
ADpsg_dt$sleepiness_std = ADpsg_dt$sleepiness + 1

sleepiness_lm = lm(
  data = ADpsg_dt, formula = sleepiness ~ sex + age + edu + townsend + whr + ad_diag)

sleepiness_df = data.frame(name=row.names(summary(sleepiness_lm)$coefficients),
                           Beta = summary(sleepiness_lm)$coefficients[,1],
                           lower = (summary(sleepiness_lm)$coefficients[,1] - summary(sleepiness_lm)$coefficients[,2]),
                           upper = (summary(sleepiness_lm)$coefficients[,1] + summary(sleepiness_lm)$coefficients[,2]),
                           p_value = summary(sleepiness_lm)$coefficients[,4])
write.csv(sleepiness_df,"data_out/sleepiness_df.csv")

sleepiness_df = subset(sleepiness_df, name != "(Intercept)")
sleepiness_df = subset(sleepiness_df, p_value <= 0.05)

ggplot(sleepiness_df, 
       aes(x=reorder(name,Beta), y=Beta, color = p_value)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 0, linetype="dotted") +
  coord_flip()+ylab("Beta values") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-50-1.png)<!-- -->

``` r
ggsave('fig_out/sleepinessAD_beta_significant_only.pdf', width = 4, height = 2)
```

#### Create an odds ratio graph

``` r
PARPsnp_AD_ageEduModels = read.csv('data_out/PARPsnp_AD_ageEduModels.csv')
PARPsnp_AD_ageEduModels$cat = 'PARPsnp_AD_ageEduModels'
PARPsnp_AD_ageEduModels = subset(PARPsnp_AD_ageEduModels, p_value <= 0.05)

PARPsnp_AD_ageEduModels_lowerADpsg = read.csv('data_out/PARPsnp_AD_ageEduModels_lowerADpsg.csv')
PARPsnp_AD_ageEduModels_lowerADpsg$cat = 'PARPsnp_AD_ageEduModels_lowerADpsg'
PARPsnp_AD_ageEduModels_lowerADpsg = subset(PARPsnp_AD_ageEduModels_lowerADpsg, p_value <= 0.05)

PARPsnp_AD_ageEduModels_upperADpsg = read.csv('data_out/PARPsnp_AD_ageEduModels_upperADpsg.csv')
PARPsnp_AD_ageEduModels_upperADpsg$cat = 'PARPsnp_AD_ageEduModels_upperADpsg'
PARPsnp_AD_ageEduModels_upperADpsg = subset(PARPsnp_AD_ageEduModels_upperADpsg, p_value <= 0.05)

PARPsnp_andSleep_in_ADpatient = read.csv('data_out/PARPsnp_andSleep_in_ADpatient.csv')
PARPsnp_andSleep_in_ADpatient$cat = 'PARPsnp_andSleep_in_ADpatient'
PARPsnp_andSleep_in_ADpatient = subset(PARPsnp_andSleep_in_ADpatient, p_value <= 0.05)

parp_snp_fig_dt = rbind(PARPsnp_AD_ageEduModels,PARPsnp_AD_ageEduModels_lowerADpsg)
parp_snp_fig_dt = rbind(parp_snp_fig_dt,PARPsnp_AD_ageEduModels_upperADpsg)
#parp_snp_fig_dt = rbind(parp_snp_fig_dt,PARPsnp_andSleep_in_ADpatient)

parp_snp_fig_dt$name = with(parp_snp_fig_dt, paste0(cat," ",snp_name))

parp_snp_fig_dt <- parp_snp_fig_dt[order(parp_snp_fig_dt$snp_name),] 

library(ggplot2)
ggplot(parp_snp_fig_dt, 
       aes(x=reorder(name,OR), y=OR)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 1, linetype="dotted") +
  coord_flip()+ylab("Odds ratio") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-51-1.png)<!-- -->

``` r
ggsave('fig_out/parp_odds_significant_only.pdf', width = 6, height = 2)
```

\#\#\#\# Create an additional graph just for the sleepiness data

``` r
rs2230484_G = lm(
    data = ukb_dt_psgAD, formula = (sleepiness) ~ sex + age + edu + townsend + whr + rs2230484_G)

rs2230484_G_sleeppiness_model_df = data.frame(name=row.names(summary(rs2230484_G)$coefficients),
                           Beta = summary(rs2230484_G)$coefficients[,1],
                           lower = (summary(rs2230484_G)$coefficients[,1] - summary(rs2230484_G)$coefficients[,2]),
                           upper = (summary(rs2230484_G)$coefficients[,1] + summary(rs2230484_G)$coefficients[,2]),
                           p_value = summary(rs2230484_G)$coefficients[,4])
write.csv(rs2230484_G_sleeppiness_model_df,"data_out/rs2230484_G_sleeppiness_model_df.csv")

rs2230484_G_sleeppiness_model_df = subset(rs2230484_G_sleeppiness_model_df, name != "(Intercept)")
#rs2230484_G_sleeppiness_model_df = subset(rs2230484_G_sleeppiness_model_df, p_value <= 0.05)

ggplot(rs2230484_G_sleeppiness_model_df, 
       aes(x=reorder(name,Beta), y=Beta, color = p_value)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 0, linetype="dotted") +
  coord_flip()+ylab("Beta values") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-52-1.png)<!-- -->

``` r
ggsave('fig_out/rs2230484_G_sleeppiness_model_significant_only.pdf', width = 4, height = 2)
```

### Generate the PDF for the PARP Human Splicing Variant (HSV) data

``` r
HSV_out = read.csv("additional_PARP_analysis/genomnis_mutations_details_rs3219134_edited.csv")
library(gridExtra)
```

    ## 
    ## Attaching package: 'gridExtra'

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     combine

``` r
pdf("fig_out/HSV_out.pdf")
grid.table(HSV_out)
dev.off()
```

    ## quartz_off_screen 
    ##                 2

## Vitamin B medications

### Curation of the drug data

``` r
med_raw = read.csv("data/medications_20003_dt.csv")
med_coding = read.csv("data/nam_coding4.tsv", 
                      sep = "\t")
med_coding$FA <- NULL
med_coding$NAD = NA
med_coding$NAD[med_coding$NAM == 1 | med_coding$vitaminB ==1] <-1
nam_metadt = subset(med_coding, !is.na(NAD))
nam_metadt
```

    ##          coding                                                meaning NAM
    ## 1683 1140867900 prolintane hydrochloride+vitamins b+c 2.5mg/5ml liquid  NA
    ## 2096 1140870914                                   nicotinamide product   1
    ## 2107 1140871004                                           vitamins b+c  NA
    ## 2110 1140871024                              vitamin b compound tablet  NA
    ## 4559 1140910670                                                 niacin   1
    ##      vitaminB multiv NAD
    ## 1683        1     NA   1
    ## 2096       NA     NA   1
    ## 2107        1     NA   1
    ## 2110        1     NA   1
    ## 4559       NA     NA   1

``` r
nrow(nam_metadt)
```

    ## [1] 5

start with NAM & niacin

``` r
nam_metadt$name = c("vit_bc","nam","vit_bc1","vit_b","niacin")

med_raw$vit_bc = apply(med_raw, 1, function(x) any(x %in% c("1140867900")))
med_raw$nam = apply(med_raw, 1, function(x) any(x %in% c("1140870914")))
med_raw$vit_bc1 = apply(med_raw, 1, function(x) any(x %in% c("1140871004")))
med_raw$vit_b = apply(med_raw, 1, function(x) any(x %in% c("1140871024")))
med_raw$niacin = apply(med_raw, 1, function(x) any(x %in% c("1140910670")))

med_out = med_raw[,c("eid",nam_metadt$name)]

write.csv(med_out,"data_out/nam_drug_subset.csv",row.names=FALSE)

#drop vit_bc because it's empty
med_out$vit_bc <- NULL

drug_dt = merge(full_dt,med_out, by = "eid")

drug_dt$sleepiness = drug_dt$sleep_dur+drug_dt$daysleep_sim-drug_dt$insomnia_sim
write.csv(drug_dt,"data_out/full_dt_AddNAM.csv",row.names=FALSE)
```

#### Descriptive stats

this takes a long time

``` r
ukb_descript_stats <- tableby(ad_diag ~ ., data =drug_dt[,2:ncol(drug_dt)])
write2word(ukb_descript_stats, "ukb_descriptStats_NAM.doc",
           keep.md = TRUE,
           quiet = TRUE, # passed to rmarkdown::render
           title = "Descriptive statistics of the UK Biobank data") # passed to summary.tableby
```

``` r
drug_dt$NAD = FALSE
drug_dt$NAD[drug_dt$nam == TRUE |drug_dt$niacin ==TRUE] <-TRUE
drug_dt$vb = FALSE
drug_dt$vb[drug_dt$vit_bc1 == TRUE |drug_dt$vit_b ==TRUE | drug_dt$vit_bc ==TRUE ] <-TRUE

drug_dt$nam_vb = FALSE
drug_dt$nam_vb[drug_dt$NAD == TRUE |drug_dt$vb ==TRUE ] <-TRUE

NAD_model =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + NAD,                   
    family = "binomial", data = drug_dt)

summary(NAD_model)
```

    ## 
    ## Call:
    ## glm(formula = ad_diag ~ sex + age + edu + townsend + whr + NAD, 
    ##     family = "binomial", data = drug_dt)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -0.3058  -0.0730  -0.0503  -0.0311   4.1527  
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)       -13.471832   0.495667 -27.179  < 2e-16 ***
    ## sexMale             0.209597   0.085456   2.453 0.014179 *  
    ## age                 0.121080   0.005065  23.905  < 2e-16 ***
    ## eduNo certificate   0.687251   0.067739  10.146  < 2e-16 ***
    ## townsend            0.039867   0.010290   3.874 0.000107 ***
    ## whr                -0.568250   0.482206  -1.178 0.238623    
    ## NADTRUE            -8.386701 113.101478  -0.074 0.940889    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 14139  on 496329  degrees of freedom
    ## Residual deviance: 13224  on 496323  degrees of freedom
    ##   (6174 observations deleted due to missingness)
    ## AIC: 13238
    ## 
    ## Number of Fisher Scoring iterations: 13

``` r
nad_participants = subset(drug_dt,NAD==TRUE)
nad_participants$ad_diag
```

    ##  [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    ## [13] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    ## [25] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    ## [37] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    ## [49] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE

none of the people who took NAM had AD

### Vitamin B and AD

\#\#\#\# Vitamin B and AD

``` r
vb_model =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + vb,                   
               family = "binomial", data = drug_dt)
summary(vb_model)
```

    ## 
    ## Call:
    ## glm(formula = ad_diag ~ sex + age + edu + townsend + whr + vb, 
    ##     family = "binomial", data = drug_dt)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -0.3059  -0.0730  -0.0503  -0.0311   4.1527  
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)       -13.470504   0.495693 -27.175  < 2e-16 ***
    ## sexMale             0.209012   0.085469   2.445 0.014466 *  
    ## age                 0.121100   0.005066  23.907  < 2e-16 ***
    ## eduNo certificate   0.687081   0.067742  10.143  < 2e-16 ***
    ## townsend            0.039914   0.010291   3.878 0.000105 ***
    ## whr                -0.569656   0.482209  -1.181 0.237465    
    ## vbTRUE             -0.138671   0.380209  -0.365 0.715319    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 14139  on 496329  degrees of freedom
    ## Residual deviance: 13224  on 496323  degrees of freedom
    ##   (6174 observations deleted due to missingness)
    ## AIC: 13238
    ## 
    ## Number of Fisher Scoring iterations: 10

\#\#\#\# Vitamin B and sleepiness

In whole population

``` r
sleepiness_lm = lm(
  data = drug_dt, formula = sleepiness ~ sex + age + edu + townsend + whr + vb)
summary(sleepiness_lm)
```

    ## 
    ## Call:
    ## lm(formula = sleepiness ~ sex + age + edu + townsend + whr + 
    ##     vb, data = drug_dt)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -7.5275 -1.1993 -0.2109  0.7627 16.6175 
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)        5.9471351  0.0287696 206.716   <2e-16 ***
    ## sexMale            0.2132944  0.0057882  36.850   <2e-16 ***
    ## age                0.0050399  0.0002686  18.761   <2e-16 ***
    ## eduNo certificate -0.0051063  0.0059038  -0.865   0.3871    
    ## townsend          -0.0122968  0.0007231 -17.005   <2e-16 ***
    ## whr                0.0244573  0.0326213   0.750   0.4534    
    ## vbTRUE            -0.0585199  0.0248346  -2.356   0.0185 *  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 1.518 on 490427 degrees of freedom
    ##   (12070 observations deleted due to missingness)
    ## Multiple R-squared:  0.006645,   Adjusted R-squared:  0.006633 
    ## F-statistic: 546.8 on 6 and 490427 DF,  p-value: < 2.2e-16

In AD cohort

``` r
AD_dt = subset(drug_dt, ad_diag == TRUE)
sleepinessAD_vb_lm = lm(
  data = AD_dt, formula = sleepiness ~ sex + age + edu + townsend + whr + vb)
summary(sleepinessAD_vb_lm)
```

    ## 
    ## Call:
    ## lm(formula = sleepiness ~ sex + age + edu + townsend + whr + 
    ##     vb, data = AD_dt)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -5.9222 -1.0451  0.0176  1.0717  8.6500 
    ## 
    ## Coefficients:
    ##                   Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)        4.84004    1.09740   4.410 1.15e-05 ***
    ## sexMale            0.24782    0.14734   1.682   0.0929 .  
    ## age                0.01456    0.01311   1.111   0.2670    
    ## eduNo certificate -0.01031    0.12150  -0.085   0.9324    
    ## townsend          -0.04086    0.01817  -2.249   0.0247 *  
    ## whr                1.11712    0.84440   1.323   0.1862    
    ## vbTRUE            -0.10806    0.66888  -0.162   0.8717    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 1.761 on 944 degrees of freedom
    ##   (54 observations deleted due to missingness)
    ## Multiple R-squared:  0.01959,    Adjusted R-squared:  0.01336 
    ## F-statistic: 3.144 on 6 and 944 DF,  p-value: 0.004668

\#\#\# Vitamin B and NAM vs AD and sleepiness

``` r
namVB_model =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb,               
              family = "binomial", data = drug_dt)
summary(namVB_model)
```

    ## 
    ## Call:
    ## glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb, 
    ##     family = "binomial", data = drug_dt)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -0.3060  -0.0730  -0.0503  -0.0311   4.1527  
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)       -13.470524   0.495694 -27.175  < 2e-16 ***
    ## sexMale             0.208961   0.085469   2.445 0.014490 *  
    ## age                 0.121101   0.005065  23.907  < 2e-16 ***
    ## eduNo certificate   0.687046   0.067742  10.142  < 2e-16 ***
    ## townsend            0.039921   0.010291   3.879 0.000105 ***
    ## whr                -0.569558   0.482211  -1.181 0.237548    
    ## nam_vbTRUE         -0.153302   0.380188  -0.403 0.686781    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 14139  on 496329  degrees of freedom
    ## Residual deviance: 13224  on 496323  degrees of freedom
    ##   (6174 observations deleted due to missingness)
    ## AIC: 13238
    ## 
    ## Number of Fisher Scoring iterations: 10

### Add PSG in data

``` r
ADpsg_dt = subset(drug_dt, !is.na(ad_psg))
ukb_dt_psg_upper = subset(ADpsg_dt, ad_psg>mean(na.omit(ADpsg_dt$ad_psg)))
ukb_dt_psg_lower = subset(ADpsg_dt, ad_psg<mean(na.omit(ADpsg_dt$ad_psg)))
```

#### High PSG

``` r
vb_model_upperPSG =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb,                   
              family = "binomial", data = ukb_dt_psg_upper)
summary(vb_model_upperPSG)
```

    ## 
    ## Call:
    ## glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb, 
    ##     family = "binomial", data = ukb_dt_psg_upper)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -0.2865  -0.0766  -0.0532  -0.0332   3.9632  
    ## 
    ## Coefficients:
    ##                    Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)       -13.30303    0.67905 -19.591  < 2e-16 ***
    ## sexMale             0.11374    0.11743   0.969   0.3328    
    ## age                 0.11811    0.00692  17.068  < 2e-16 ***
    ## eduNo certificate   0.66193    0.09367   7.066 1.59e-12 ***
    ## townsend            0.04261    0.01420   3.001   0.0027 ** 
    ## whr                -0.35032    0.66373  -0.528   0.5976    
    ## nam_vbTRUE         -1.49330    1.00158  -1.491   0.1360    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 7363.3  on 238520  degrees of freedom
    ## Residual deviance: 6897.4  on 238514  degrees of freedom
    ##   (1142 observations deleted due to missingness)
    ## AIC: 6911.4
    ## 
    ## Number of Fisher Scoring iterations: 10

``` r
sleepiness_vb_model_upperPSG =lm(formula = sleepiness ~ sex + age + edu + townsend + whr + nam_vb, data = ukb_dt_psg_upper)
summary(sleepiness_vb_model_upperPSG)
```

    ## 
    ## Call:
    ## lm(formula = sleepiness ~ sex + age + edu + townsend + whr + 
    ##     nam_vb, data = ukb_dt_psg_upper)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -7.4055 -1.2029 -0.2199  0.7541 15.8020 
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)        5.9915745  0.0413523 144.891   <2e-16 ***
    ## sexMale            0.2116454  0.0083271  25.416   <2e-16 ***
    ## age                0.0041874  0.0003855  10.861   <2e-16 ***
    ## eduNo certificate  0.0041249  0.0085679   0.481   0.6302    
    ## townsend          -0.0116631  0.0010443 -11.168   <2e-16 ***
    ## whr                0.0338542  0.0470451   0.720   0.4718    
    ## nam_vbTRUE        -0.0980806  0.0350169  -2.801   0.0051 ** 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 1.513 on 235567 degrees of freedom
    ##   (4089 observations deleted due to missingness)
    ## Multiple R-squared:  0.006317,   Adjusted R-squared:  0.006292 
    ## F-statistic: 249.6 on 6 and 235567 DF,  p-value: < 2.2e-16

\#\#\#\# Low PSG - not show

``` r
vb_model_lowerPSG =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb,
                       family = "binomial", data = ukb_dt_psg_lower)
summary(vb_model_lowerPSG)
```

    ## 
    ## Call:
    ## glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb, 
    ##     family = "binomial", data = ukb_dt_psg_lower)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -0.2761  -0.0676  -0.0458  -0.0278   4.1542  
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)       -13.840970   0.860780 -16.080  < 2e-16 ***
    ## sexMale             0.372656   0.148646   2.507   0.0122 *  
    ## age                 0.124935   0.008761  14.260  < 2e-16 ***
    ## eduNo certificate   0.683682   0.117451   5.821 5.85e-09 ***
    ## townsend            0.032469   0.018039   1.800   0.0719 .  
    ## whr                -0.710079   0.839523  -0.846   0.3977    
    ## nam_vbTRUE          0.617931   0.452809   1.365   0.1724    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 4823.4  on 192142  degrees of freedom
    ## Residual deviance: 4496.4  on 192136  degrees of freedom
    ##   (941 observations deleted due to missingness)
    ## AIC: 4510.4
    ## 
    ## Number of Fisher Scoring iterations: 10

``` r
sleepiness_nam_model_lowerPSG =lm(formula = sleepiness ~ sex + age + edu + townsend + whr + nam_vb, data = ukb_dt_psg_lower)
summary(sleepiness_nam_model_lowerPSG)
```

    ## 
    ## Call:
    ## lm(formula = sleepiness ~ sex + age + edu + townsend + whr + 
    ##     nam_vb, data = ukb_dt_psg_lower)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -7.5262 -1.2061 -0.2173  0.7562 16.6163 
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)        5.9772741  0.0460508 129.797   <2e-16 ***
    ## sexMale            0.2096439  0.0092809  22.589   <2e-16 ***
    ## age                0.0048170  0.0004289  11.231   <2e-16 ***
    ## eduNo certificate -0.0105953  0.0095340  -1.111    0.266    
    ## townsend          -0.0110753  0.0011634  -9.520   <2e-16 ***
    ## whr                0.0110245  0.0523561   0.211    0.833    
    ## nam_vbTRUE        -0.0298967  0.0397634  -0.752    0.452    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 1.513 on 189856 degrees of freedom
    ##   (3221 observations deleted due to missingness)
    ## Multiple R-squared:  0.006187,   Adjusted R-squared:  0.006156 
    ## F-statistic:   197 on 6 and 189856 DF,  p-value: < 2.2e-16

\#\#\# Plot Vitamin B graphs

#### Vitamin B & AD (General pop)

``` r
namVB_model =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb,               
              family = "binomial", data = drug_dt)

namVB_model_df = data.frame(name=row.names(summary(namVB_model)$coefficients),
                           OR = exp(summary(namVB_model)$coefficients[,1]),
                           lower = exp(summary(namVB_model)$coefficients[,1] - summary(namVB_model)$coefficients[,2]),
                           upper = exp(summary(namVB_model)$coefficients[,1] + summary(namVB_model)$coefficients[,2]),
                           p_value = summary(namVB_model)$coefficients[,4])
write.csv(namVB_model_df,"data_out/namVB_model_df.csv")

namVB_model_df = subset(namVB_model_df, name != "(Intercept)")

ggplot(namVB_model_df, 
       aes(x=reorder(name,OR), y=OR)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 1, linetype="dotted") +
  coord_flip()+ylab("Odds ratio") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-68-1.png)<!-- -->

``` r
ggsave('fig_out/vitaminB_AD_model.pdf', width = 6, height = 2)
```

#### Vitamin B & sleepiness (General pop)

``` r
namVB_sleeppiness_model =lm(formula = sleepiness ~ sex + age + edu + townsend + whr + nam_vb, data = drug_dt)
#summary(namVB_sleeppiness_model)

namVB_sleeppiness_model_df = data.frame(name=row.names(summary(namVB_sleeppiness_model)$coefficients),
                           Beta = summary(namVB_sleeppiness_model)$coefficients[,1],
                           lower = (summary(namVB_sleeppiness_model)$coefficients[,1] - summary(namVB_sleeppiness_model)$coefficients[,2]),
                           upper = (summary(namVB_sleeppiness_model)$coefficients[,1] + summary(namVB_sleeppiness_model)$coefficients[,2]),
                           p_value = summary(namVB_sleeppiness_model)$coefficients[,4])
write.csv(namVB_sleeppiness_model_df,"data_out/namVB_sleeppiness_model_df.csv")

namVB_sleeppiness_model_df = subset(namVB_sleeppiness_model_df, name != "(Intercept)")

ggplot(namVB_sleeppiness_model_df, 
       aes(x=reorder(name,Beta), y=Beta, color = p_value)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 0, linetype="dotted") +
  coord_flip()+ylab("Beta values") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-69-1.png)<!-- -->

``` r
ggsave('fig_out/namVB_sleeppiness_model.pdf', width = 4, height = 2)
```

#### Vitamin B & AD (high PSG)

``` r
vb_model_upperPSG =glm(formula = ad_diag ~ sex + age + edu + townsend + whr + nam_vb,                   
              family = "binomial", data = ukb_dt_psg_upper)
#summary(vb_model_upperPSG)

vb_model_upperPSG_df = data.frame(name=row.names(summary(vb_model_upperPSG)$coefficients),
                           OR = exp(summary(vb_model_upperPSG)$coefficients[,1]),
                           lower = exp(summary(vb_model_upperPSG)$coefficients[,1] - summary(vb_model_upperPSG)$coefficients[,2]),
                           upper = exp(summary(vb_model_upperPSG)$coefficients[,1] + summary(vb_model_upperPSG)$coefficients[,2]),
                           p_value = summary(vb_model_upperPSG)$coefficients[,4])
write.csv(vb_model_upperPSG_df,"data_out/vb_model_upperPSG_df.csv")

vb_model_upperPSG_df = subset(vb_model_upperPSG_df, name != "(Intercept)")

ggplot(vb_model_upperPSG_df, 
       aes(x=reorder(name,OR), y=OR)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 1, linetype="dotted") +
  coord_flip()+ylab("Odds ratio") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-70-1.png)<!-- -->

``` r
ggsave('fig_out/vitaminb_model_upperPSG.pdf', width = 6, height = 2)
```

#### Vitamin B & sleepiness (high PSG)

``` r
sleepiness_vb_model_upperPSG =lm(formula = sleepiness ~ sex + age + edu + townsend + whr + nam_vb, data = ukb_dt_psg_upper)
#summary(sleepiness_vb_model_upperPSG)

sleepiness_vb_model_upperPSG_df = data.frame(name=row.names(summary(sleepiness_vb_model_upperPSG)$coefficients),
                           Beta = summary(sleepiness_vb_model_upperPSG)$coefficients[,1],
                           lower = (summary(sleepiness_vb_model_upperPSG)$coefficients[,1] - summary(sleepiness_vb_model_upperPSG)$coefficients[,2]),
                           upper = (summary(sleepiness_vb_model_upperPSG)$coefficients[,1] + summary(sleepiness_vb_model_upperPSG)$coefficients[,2]),
                           p_value = summary(sleepiness_vb_model_upperPSG)$coefficients[,4])
write.csv(sleepiness_vb_model_upperPSG_df,"data_out/sleepiness_vb_model_upperPSG_df.csv")

sleepiness_vb_model_upperPSG_df = subset(sleepiness_vb_model_upperPSG_df, name != "(Intercept)")

ggplot(sleepiness_vb_model_upperPSG_df, 
       aes(x=reorder(name,Beta), y=Beta, color = p_value)) + 
  geom_errorbar(aes(ymin=lower, ymax=upper),
                width=0,                    # Width of the error bars
                position=position_dodge(.9), color = "grey", size = 1) +
  geom_point(shape=21, size = 2, color = 'red', fill = "red") +
  theme_classic() + 
  geom_hline(yintercept = 0, linetype="dotted") +
  coord_flip()+ylab("Beta values") + xlab("")
```

![](Abeta_parp_nam_UKB_files/figure-gfm/unnamed-chunk-71-1.png)<!-- -->

``` r
ggsave('fig_out/sleepiness_vb_model_upperPSG_beta.pdf', width = 4, height = 2)
```
