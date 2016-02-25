\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{softeng}[2016/2/25 Classe per il progetto di ingegneria del software]

\newif\if@utfdocument %\@utfdocumentfalse

% apparently this is how you optionally require a package
\DeclareOption{utf8}{
	\@utfdocumenttrue
}

\DeclareOption*{
	\PassOptionsToClass{\CurrentOption}{article}
}

\ProcessOptions\relax
% done processing options, do what you want

\LoadClass[11pt,a4paper,twocolumn]{article}

% optional inclusion of utf8 input encoding package
\if@utfdocument
	\RequirePackage[utf8]{inputenc}
\fi

\RequirePackage[T1]{fontenc}
\RequirePackage[italian]{babel}
\RequirePackage{fullpage}
\RequirePackage{parskip}
\RequirePackage{hyperref}
\RequirePackage{nameref}

\RequirePackage{titling}
\RequirePackage{fancyhdr}

\author{Artemio Ageev \and Luigi Iandolo \and Michele Laurenti}

\pagestyle{fancy}
\fancyhf{}
\rhead{\leftmark}
\lhead{\thetitle}
\rfoot{\thepage}
\lfoot{\theauthor}

% fancyhdr asked for this
\setlength{\headheight}{14pt}
\setlength{\headsep}{19pt}

\RequirePackage[pdftex]{graphicx}

\RequirePackage{titling}

\setlength{\droptitle}{-8em}

\endinput


