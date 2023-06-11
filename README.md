![image](https://github.com/SwiftGlitxh/GWTX/assets/72777943/b10e365e-911b-4f13-a92e-f79d99c101c7)

# GWTX (beta)

GWTX is a console that will be designed for exploiting targets and performing various network-related tasks. It provides a command-line interface for executing commands and managing options.

## Prerequisites

Before using the GWTX Console, ensure that the following packages are installed:

- `os`
- `subprocess`
- `cmd`
- `colorama`

## UPDATES
+ FTP - File Transfer Protocol has now been added 
+ SSH -  Secure Socket Shell has been added 
+ Show payloads | use -h has been changed

## Installation

1. Clone the repository:

`git clone https://github.com/SwiftGlitxh/GWTX`

Change into the project directory:
`cd GWTX`

## Usage
To start the GWTX Console, run the following command:
`python3 gwtx.py`
The console will display a banner and prompt you with a command prompt (gwtx >).
## Available Commands
The following commands are available in the GWTX Console:
```
Commands                   Description
========                   ===========
help                    Show available commands
exploit <target>        Exploit a target
set ip <value>          Set the IP address
set payload <value>     Set payload
show payloads           Show payloads available
scan                    Scan ip for open ports
clear                   Clear screen
exit                    Exit the console 
```
Use the help command to see the full list of available commands and their descriptions.

## Example Usage
Here's an example workflow to help you get started:

```python
                               _,.-------.,_
                             ,;~'             '~;,
                           ,;                     ;,
                          ;                         ;
                         ,'                         ',
                        ,;                           ;,
                        ; ;      .           .      ; ;
                        | ;   ______       ______   ; |
                        |  `/~"     ~" . "~     "~'  |
                        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                         |   |        ):(        |   |
                         |   l       / | \       !   |
                         .~  (__,.--" .^. "--.,__)  ~.
                         |     ---;' / | \ `;---     |
                          \__.       \/^\/       .__/
                           V| \                 / |V
                            | |T~\___!___!___/~T| |
                            | |`IIII_I_I_I_IIII'| |
                            |  \,III I I I III,/  |
                             \   `~~~~~~~~~~'    /
                               \   .       .   /
                                 \.    ^    ./
                                   ^~~~^~~~^      
                      .Gt                                                                                           
                     j#W:           ;        GEEEEEEEL                                                              
                   ;K#f           .DL        ,;;L#K;;.:KW,      L                                                   
                 .G#D.    f.     :K#L     LWL   t#E    ,#W:   ,KG                                                   
                j#K;      EW:   ;W##L   .E#f    t#E     ;#W. jWi                                                    
              ,K#f   ,GD; E#t  t#KE#L  ,W#;     t#E      i#KED.                                                     
               j#Wi   E#t E#t f#D.L#L t#K:      t#E       L#W.                                                      
                .G#D: E#t E#jG#f  L#LL#G        t#E     .GKj#K.                                                     
                  ,K#fK#t E###;   L###j         t#E    iWf  i#K.                                                    
                    j###t E#K:    L#W;          t#E   LK:    t#E                                                    
                     .G#t EG      LE.            fE   i       tDj                                                   
                       ;; ;       ;@              :                                                                 
                                                                                                                    
    *** Welcome to the GWTX console! Type 'help' for available commands ***                                         

[       This tool is a custom console designed for exploiting targets           ]
[    and performing various network-related tasks.It provides a command-line    ]
[         interface for executing commands and managing options.                ]
gwtx > set ip 157.122.154.154
[info] --> Set ip to 157.122.154.154
gwtx > set payload locate
[info] --> Set payload to locate
gwtx > exploit
[info] Starting Exploit On  157.122.154.154
[info] Running payload 'tools/locate.py' against target: 157.122.154.154
IP Location Information:
IP Address: 157.122.154.154
Country: China
City: Shenzhen
Zip Code: 
Latitude: 22.5431
Longitude: 114.058
[complete] Scan Complete

```

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the [MIT License.](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
