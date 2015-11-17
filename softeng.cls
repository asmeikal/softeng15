\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{softeng}[2015/11/16 Classe per il progetto di ingegneria del software]

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

\LoadClass[11pt,a4paper]{article}

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

\pagestyle{fancy}
\fancyhf{}
\rhead{\leftmark}
\lhead{\thetitle}
\rfoot{\thepage}
\lfoot{\theauthor}

% fancyhdr asked for this
\setlength{\headheight}{14pt}

\RequirePackage[pdftex]{graphicx}

\author{Artemio Ageev \and Luigi Iandolo \and Michele Laurenti}

\endinput


