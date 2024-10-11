
from llama_cpp import Llama

# Load the model
model_path = "/app/model/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf"
llm = Llama(model_path=model_path, n_ctx=4096, n_threads=32)

def generate_text(prompt, max_tokens=100):
    output = llm(prompt, max_tokens=max_tokens, echo=True)
    return output['choices'][0]['text']

if __name__ == "__main__":
    prompt = """Review this raw text and extract all sensitive information, including API tokens, passwords, keys, and any unusual command syntax that might be sensitive. Highlight any anomalies or patterns that resemble password-like strings.
Give me the original text as it appears, without any formatting or processing.
Find any suspicious flags, arguments, or commands that resemble password-like strings.
Only write as output the sensitive information and nothing more.

raw text:
whoami -i --version --version -s ~/Documents
more -h grep error
curl -l -r file.txt
cat --help -f -p -f > output.txt
telemetry.py -u -u -t
awk -c -q --version -t 2>/dev/null
scp --version -n -t | sort
ifconfig -x -t '*.py'
tar -r -o | uniq
cal --version -o -a -a
head --help --help -a -i *.log
sshpass -q --help -g -s /home/user
free -a -n > output.txt
whoami --help -s -q -a | wc -l
touch -x -o -a
cd -r -c -g > output.txt
telemetry.py -n -f --version -v -u "monitor" -P "TeleIsAwesome!" &
touch -n -i -f | wc -l
grep -l -n -a &
tail -f -u -h $(date +%Y-%m-%d)
less -d -p -q | wc -l
cal --help -x -o grep error
find --help -a -r &
sed -p -n |
ssh -v -d -x $HOME
kill -g -a | wc -l
cal -a *.log
telemetry.py -d -c -v 2>&1
curl -o -g -g $(date +%Y-%m-%d)
sort -c -h -d $HOME
ifconfig --version --help
tar -u -x grep error
last -f -t $(date +%Y-%m-%d)
ifconfig -l -i -l -q /etc
df -r -g -l -u | wc -l
wc -h
ping -d -o -o -s |
wc -v -t --version 2>&1
wget -s -r |
cd -i -t -n *.log
ps -l -s
netstat -o | uniq
tail -t -n
who -l -l -d 2>&1
less -s -p -l -l file.txt
curl -s -h -i &
tail --version -r -h grep error
free -o -t -o *.log
rm -i -r 2>&1
sort --version -g -n $(date +%Y-%m-%d)
wget -s -f $(date +%Y-%m-%d)
awk -a -p -g -i | uniq
pwd -c -r | wc -l
ifconfig --version -g --help | uniq
gzip -i -v -a > output.txt
echo -q -r
gzip -g -a '*.py'
date -s -h -s |
w -o -o /usr/bin
sshpass -u ohad -p "Dooshik21#2020"
netstat -i -p -u -i
mkdir -d -u -i -x
uniq -h -p grep error
less -n -g -p -a file.txt
rm -s -l -u -r grep error
ifconfig -c -x -h 2>&1
top -u -q
scp -d -l *.log
last -x -i -u grep error
gzip -v -d -s 2>&1
ls -t -p -s 2>&1
cal -t -x | sort
uniq --version -d -o -f $USER
find -n grep error
w -n -p -p -g *.log
echo -h -x -f
pwd --help -h &
wget -d -x -a $HOME
find -s -r -q 2>&1
ifconfig -s -r -u -x &
head -q -o -o --help
wget -p -f -t -p $USER
last -u -i -d | wc -l
mkdir -c -g *.log
cp -x -d -x | uniq
tail -c -g -c $HOME
cal -l -s -c -a | uniq
ping -u -n -n /etc
cat -c -o -x $USER
ping -c -h -i /var/log
more --version -h -v | sort
less -i -l -x $USER
curl -q -f file.txt
mkdir --version -i -o $USER
last -c -a -f | uniq
df -x -d -r -r ~/Documents
ssh -s -q -x -v 2>/dev/null
curl -r -u
tail -a -r -q -i $HOME
pwd -h -p 2>/dev/null
ssh -r --version -v *.log
date -t -o |
top -q -l -a -g /usr/bin
touch -u --version 2>/dev/null
less -d -s $HOME
wget -u -n 2>&1
sed -o --help -i 2>&1
cal --help -h -n
scp -f -v -i
cat -o -s
grep -t /etc
wc -o -r | wc -l
history -o -s -l | uniq
gzip -x -l $HOME
who -l /usr/bin
sort -h -h
scp -q -a $(date +%Y-%m-%d)
top -o --help -n -x /usr/bin
mv -s -a -l '*.py'
touch -s --version -t /var/log
gzip -v -r &
df -q -x *.log
history -p --help -v -n $USER
head -h -p -c -r ~/Documents
df -c -i -t 2>/dev/null
less -x -q --version $USER
more -f |
sed -u -l /home/user"""
    #prompt = input("Enter a prompt (or 'quit' to exit): ")
    # if prompt.lower() == 'quit':
        # break
    generated_text = generate_text(prompt)
    print("Generated text:", generated_text)