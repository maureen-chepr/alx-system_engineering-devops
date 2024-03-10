**Postmortem: Web Stack Outage Incident**

**Duration:**
- The outage occurred from March 10, 2024, 14:45 UTC to March 10, 2024, 18:30 UTC.

**Impact:**
- The outage affected the primary web service, resulting in a 54% degradation in response times.
- Users experienced slow loading times and intermittent errors, impacting their ability to access critical features.

**Root Cause:**
- A database connection pool exhaustion due to a misconfigured connection limit during peak EAT (Eastern Africa Time) usage.

**Timeline:**
- **14:45 UTC:** Issue detected through automated monitoring alerts indicating increased response times.
- **14:50 UTC:** Engineering team received automated alert notifications and initiated initial investigation.
- **15:10 UTC:** Assumed potential server overload; scaled up server instances to handle increased load.
- **15:45 UTC:** Despite scaling efforts, response times continued to degrade; database connection pool investigated.
- **16:30 UTC:** Identified the misconfiguration in the database connection pool settings.
- **17:00 UTC:** Misleadingly explored potential DDoS attack due to unusual traffic patterns; later ruled out.
- **17:30 UTC:** Escalated incident to Database and Networking teams for further assistance.
- **18:00 UTC:** Root cause confirmed as connection pool exhaustion; corrective measures initiated.
- **18:30 UTC:** Service fully restored after adjusting the database connection pool settings.

**Root Cause and Resolution:**
- **Root Cause:** The misconfiguration in the database connection pool settings led to a rapid exhaustion of available connections, causing a 54% degradation in response times during EAT.
- **Resolution:** Adjusted the database connection pool settings to allow for a higher connection limit, preventing future exhaustion during peak usage, especially in EAT. Conducted a thorough review of other critical system configurations to identify and rectify potential misconfigurations contributing to peak-time degradation.

**Corrective and Preventative Measures:**
- **Improvements/Fixes:**
  - Implement automated checks and alerts for critical configuration parameters, specifically focusing on peak usage times such as EAT.
  - Conduct a comprehensive review of all system configurations, with emphasis on optimizing for peak usage periods.
- **Tasks:**
  - Enhance monitoring specifically for peak usage periods like EAT, with thresholds and alerts tailored to detect abnormalities during those times.
  - Conduct a post-incident review to identify areas for improvement in incident response and escalation procedures, especially during peak hours.
  - Establish regular training sessions for the operations team to enhance their ability to quickly identify and troubleshoot configuration-related issues.
  - Enhance documentation for critical system configurations, emphasizing their impact during peak usage, to facilitate a more efficient resolution of similar incidents in the future.
  - Conduct a capacity planning review to ensure that the infrastructure can adequately handle peak loads without sacrificing performance, especially during EAT.
