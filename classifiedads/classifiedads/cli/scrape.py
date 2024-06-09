import subprocess

def scrape_data(id:str):
    p = subprocess.run(f'scrapy crawl ads -a cid={id} -O results.json',
                    shell=True, check=True,
                    capture_output=True, encoding='utf-8')
    print(f'Command {p.args} exited with {p.returncode} code, output: \n{p.stdout}')