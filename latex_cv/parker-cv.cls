\ProvidesClass{parker-cv}[2015/12/01 CV class]
\NeedsTeXFormat{LaTeX2e}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Based on Friggeris CV class                 %
% Modified by Shane Parker                    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption{resume}{\def\@cv@resume{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass{article}


%%%%%%%%%%
% Colors %
%%%%%%%%%%

\RequirePackage{xcolor}

\definecolor{white}{RGB}{255,255,255}

\definecolor{darkgray}{HTML}{333333}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{lightgray}{HTML}{999999}

\definecolor{green}{HTML}{C2E15F}
\definecolor{orange}{HTML}{FDA333}
\definecolor{purple}{HTML}{D3A4F9}
\definecolor{red}{HTML}{FB4485}
\definecolor{blue}{HTML}{6CE0F1}

\ifdefined\@cv@print
  \colorlet{green}{gray}
  \colorlet{orange}{gray}
  \colorlet{purple}{gray}
  \colorlet{brown}{gray}
  \colorlet{red}{gray}
  \colorlet{blue}{gray}
  \colorlet{fillheader}{white}
  \colorlet{header}{gray}
\else
  \colorlet{fillheader}{gray}
  \colorlet{header}{gray}
\fi
\colorlet{textcolor}{gray}
\colorlet{headercolor}{gray}

%%%%%%%%%
% Fonts %
%%%%%%%%%

\RequirePackage[quiet]{fontspec}
\RequirePackage{unicode-math}
\RequirePackage{amsmath}

\newfontfamily\bodyfont[]{Helvetica Neue}
\newfontfamily\thinfont[]{Helvetica Neue Light}
\newfontfamily\headingfont[]{Helvetica Neue Condensed Bold}

\defaultfontfeatures{Mapping=tex-text}
\setmainfont[Mapping=tex-text, Color=textcolor]{Helvetica Neue Light}

%\setmathfont{XITS Math}

%%%%%%%%%%
% Header %
%%%%%%%%%%

\RequirePackage{tikz}

\newcommand{\rolefont}{%
  \fontsize{14pt}{24pt}\selectfont%
  \thinfont%
  \color{white}%
}
\newcommand{\timesize}{\fontsize{10pt}{12pt}\selectfont}

\newcommand{\header}[6]{%
  %\begin{tikzpicture}[remember picture,overlay]
  %  \node [rectangle, anchor=north, minimum width=\paperwidth, minimum height=3.5cm] (box) at (current page.north){};
  %  \node [rectangle, anchor=south, minimum width=\paperwidth-4cm, minimum height=2cm] (innerbox) at (box.south){};
  %  \node [anchor=west] (shanem) at (innerbox.west) {%
  %    \fontsize{18pt}{18pt}\color{header}%
  %    {\thinfont #1} {\bodyfont #2}
  %  };
  %  \node[anchor=north east] (email) at (innerbox.north east) {%
  %    \fontsize{10pt}{10pt}\color{header}
  %    {\thinfont e-mail: #3}
  %  };
  %  \node[anchor=east] (web) at (innerbox.east) {%
  %    \fontsize{10pt}{10pt}\color{header}
  %    {\thinfont web: #4}
  %  };
  %  \node[anchor=south east] (ph) at (innerbox.south east) {%
  %    \fontsize{10pt}{10pt}\color{header}
  %    {\thinfont ph: #5}
  %  };
  %\end{tikzpicture}
  %\vspace{1.5cm}
{ \large
  \noindent \textbf{Shane M. Parker, PhD} } \hfill { \small (#6) }\\

\begin{minipage}{0.7\textwidth}
  \noindent Frank Hovorka Assistant Professor of Chemistry \\
  \noindent Case Western Reserve University \\
  \noindent Department of Chemistry \\
  \noindent 10900 Euclid Ave., Cleveland, OH 44106
\end{minipage}
\begin{minipage}{0.3\textwidth}
  \noindent web: quantumparker.com \\
  \noindent ph: (216) 368-3697 \\
  \noindent orcid: \href{https://orcid.org/0000-0002-1110-3393}{0000-0002-1110-3393} \\
  \noindent scholar: \href{https://scholar.google.com/citations?user=OqC2Vc8AAAAJ&hl=en}{OqC2Vc8AAAAJ}
\end{minipage}
}


%%%%%%%%%%%%%
% Structure %
%%%%%%%%%%%%%
\RequirePackage{parskip}

\newcounter{colorCounter}
\def\@sectioncolor#1#2#3{%
  {%
    \color{%
      \ifcase\value{colorCounter}%
        blue\or%
        red\or%
        orange\or%
        green\or%
        purple\or%
        brown\else%
        headercolor\fi%
    } #1#2#3%
  }%
  \stepcounter{colorCounter}%
}

\renewcommand{\section}[1]{
  \par\vspace{\parskip}
  {%
    \large\headingfont\color{headercolor}%
    \@sectioncolor #1%
  }
  %\par\vspace{\parskip}
}

\renewcommand{\subsection}[1]{
  \par\vspace{.5\parskip}%
  {\Large\headingfont\color{headercolor} #1}
  \par\vspace{.25\parskip}%
}

\renewcommand{\subsubsection}[2]{
  \par\vspace{.5\parskip}%
  {\Large\headingfont\color{headercolor} #2}
  \par\vspace{.25\parskip}%
}

\pagestyle{empty}


%%%%%%%%%%%%%%%%%%%%
% List environment %
%%%%%%%%%%%%%%%%%%%%

\RequirePackage{longtable}
\RequirePackage{tabu}

\newlength{\timelength}
\newlength{\desclength}

\ifdefined\@cv@resume
  \setlength{\timelength}{2.25cm}
  \setlength{\desclength}{11.5cm}
\else
  \setlength{\timelength}{2.25cm}
  \setlength{\desclength}{15.35cm}
\fi

\setlength{\tabcolsep}{0pt}
\newenvironment{entrylist}{%
  \begin{longtabu}{@{\extracolsep{\fill}}ll}
}{%
  \end{longtabu}
  \vspace{-2em}
}
\renewcommand{\bfseries}{\headingfont\color{headercolor}}

\newcommand{\entry}[5][0.5\parsep]{%
  \parbox[t]{\timelength}{\timesize #2}&\parbox[t]{\desclength}{%
    \textbf{#3}%
    \hfill%
    {\footnotesize\addfontfeature{Color=lightgray} #4}\\%
    #5\vspace{#1}%
  }\\
}

%%%%%%%%%%%%%%
% Side block %
%%%%%%%%%%%%%%

\ifdefined\@cv@resume
  \RequirePackage[absolute,overlay]{textpos}
  \setlength{\TPHorizModule}{1cm}
  \setlength{\TPVertModule}{1cm}
  \newenvironment{aside}{%
    \let\oldsection\section
    \renewcommand{\section}[1]{
      \par\vspace{\baselineskip}{\Large\headingfont\color{headercolor} ##1}\vspace{0.5em}
    }
    \begin{textblock}{3.6}(1.5, 3.6)
    \begin{flushright}
    \obeycr
  }{%
    \restorecr
    \end{flushright}
    \end{textblock}
    \let\section\oldsection
  }
\fi

%%%%%%%%%%%%%%%%
% Other tweaks %
%%%%%%%%%%%%%%%%

\ifdefined\@cv@resume
  \RequirePackage[left=6.1cm,top=2cm,right=1.5cm,bottom=2.5cm,nohead,nofoot]{geometry}
\else
  \RequirePackage[left=1.5cm,top=2cm,right=1.5cm,bottom=2.5cm,nohead,nofoot]{geometry}
\fi
\RequirePackage{hyperref}
\hypersetup{
    colorlinks=false,
    linkcolor=red,
    citecolor=red,
    filecolor=red,
    urlcolor = red}

% A fix for \href{}{} colors not working with fontspec
\makeatletter
\def\HyColor@@@@UseColor#1\@nil{\addfontfeatures{Color=#1}}
\makeatother
