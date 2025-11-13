thonimport requests
from puppeteer import launch

async def scrape_jobs(search_url, max_items=100):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(search_url)
    
    job_listings = []
    
    # Pagination handling
    current_page = 1
    while len(job_listings) < max_items:
        await page.goto(f"{search_url}&page={current_page}")
        
        # Extract job data
        jobs = await page.querySelectorAll('.job_listing')
        for job in jobs:
            title = await job.querySelector('.job_title')
            description = await job.querySelector('.job_description')
            company = await job.querySelector('.company_name')
            location = await job.querySelector('.location')
            
            job_listings.append({
                "title": title,
                "description": description,
                "company": company,
                "location": location,
                "url": await job.querySelector('a').getProperty('href')
            })
        
        if len(job_listings) >= max_items:
            break
        
        current_page += 1
    
    await browser.close()
    return job_listings