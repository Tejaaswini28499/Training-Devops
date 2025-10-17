1. What’s the difference between Edge-Optimized, Regional, and Private APIs?

AWS API Gateway has **three endpoint types**: **Edge-Optimized**, **Regional**, and **Private**. The difference lies in **where the API is accessible** and **how requests are routed**.

---

### 1️⃣ **Edge-Optimized API**

* **Purpose:** Best for APIs accessed **globally by clients from different locations**.
* **Routing:** Requests are routed through **Amazon CloudFront (AWS’s global CDN)**. This reduces latency for clients far from the API region.
* **Use Case:** Public APIs used by users all over the world, e.g., mobile apps or websites with global traffic.
* **Cost:** Slightly higher because of CloudFront.

---

### 2️⃣ **Regional API**

* **Purpose:** Best for APIs accessed **from clients in the same region** or when you want to put **your own CloudFront distribution in front**.
* **Routing:** Requests go directly to the API Gateway in a **specific AWS region**, without automatic CloudFront distribution.
* **Use Case:** Internal or regional APIs, e.g., backend services in the same AWS region or for multi-region architectures with your own CDN.
* **Cost:** Usually cheaper than Edge-Optimized.

---

### 3️⃣ **Private API**

* **Purpose:** Only accessible from **inside your VPC** using **VPC endpoints (AWS PrivateLink)**.
* **Routing:** Not accessible over the public internet; only via **VPC connections**.
* **Use Case:** Internal services, microservices, or APIs that must **never be exposed publicly**.
* **Security:** Can restrict access completely to private networks, very secure.

---

### ✅ Summary Table

| Type           | Accessibility            | Routing                    | Use Case                                  |
| -------------- | ------------------------ | -------------------------- | ----------------------------------------- |
| Edge-Optimized | Public, global clients   | Through CloudFront (CDN)   | Global public APIs                        |
| Regional       | Public, regional clients | Directly to regional API   | Regional or internal APIs with custom CDN |
| Private        | Private within VPC       | VPC endpoint (PrivateLink) | Internal APIs, highly secure              |

---

💡 **Tip:**

* If your API serves **worldwide users**, go **Edge-Optimized**.
* If your API serves **users in a single region** or you want **custom caching/CDN**, go **Regional**.
* If your API is **internal-only**, go **Private**.

---

How do you handle request throttling and quotas in API Gateway?
In **AWS API Gateway**, **throttling** and **quotas** are mechanisms to **protect your APIs from overuse** and to **control client traffic**. Let me explain both clearly and how you handle them:

---

## **1️⃣ Throttling**

* **Purpose:** Prevents clients from sending too many requests **in a short period**, protecting your backend.
* **How it works:**

  * API Gateway limits **requests per second (RPS)** and **burst capacity**.

    * **Rate limit:** The steady-state request rate (e.g., 100 RPS).
    * **Burst limit:** Extra capacity for short spikes (e.g., 200 requests).
* **Scope:** Can be applied at:

  * **Stage level** (all clients to a stage)
  * **Method level** (specific API methods)
  * **Usage plan** (per API key)
* **Example:**

  * A stage is configured with 100 RPS and a burst of 200. Any requests above this are throttled and return **HTTP 429 Too Many Requests**.

---

## **2️⃣ Quotas**

* **Purpose:** Limit the **total number of requests a client can make over a period** (day, week, month).
* **How it works:**

  * Quotas are **enforced via usage plans**.
  * Usage plans are associated with **API keys**.
  * You can set:

    * **Limit:** Max requests (e.g., 10,000 per month)
    * **Time period:** Day, week, or month
* **Example:**
  Client with API key `123` has a quota of 10,000 requests/month. Once exceeded, API Gateway returns **HTTP 429 Too Many Requests** until quota resets.

---

## **3️⃣ How to configure**

1. **Create a Usage Plan**

   * Define throttling and quota limits.
2. **Associate API Stage**

   * Attach the API stage (like `/v1`) to the usage plan.
3. **Create API Key**

   * Assign API keys to clients.
4. **Attach API Key to Usage Plan**

   * Ensures throttling/quotas are applied per client.

---

### **Key Notes**

* **Throttling:** protects **short-term spikes** → RPS & burst.
* **Quota:** protects **long-term usage** → daily/weekly/monthly limits.
* **If no API key / usage plan:** Stage-level throttling can still protect your API.

---

How do you enable CORS in API Gateway?
Enabling **CORS (Cross-Origin Resource Sharing)** in **AWS API Gateway** allows your API to be called from **web browsers running on a different domain**. Here’s a clear breakdown:

---

## **1️⃣ What CORS Does**

* Browsers restrict requests to a **different domain** for security (same-origin policy).
* **CORS** tells the browser: “It’s okay, this API allows requests from this origin.”

Key HTTP headers involved:

* `Access-Control-Allow-Origin` → Which domains can call the API
* `Access-Control-Allow-Methods` → Allowed HTTP methods (GET, POST, etc.)
* `Access-Control-Allow-Headers` → Allowed custom headers

---

## **2️⃣ How to Enable CORS in API Gateway**

### **A. Using the Console**

1. Go to your **API Gateway** → select your API → **Resources**.
2. Select the **resource/method** (e.g., `/users` → GET).
3. Click **Actions → Enable CORS**.
4. Configure:

   * **Allowed Origins:** `*` for all domains or specific domains like `https://example.com`
   * **Allowed Methods:** GET, POST, PUT, etc.
   * **Allowed Headers:** e.g., `Content-Type,X-Amz-Date,Authorization,X-Api-Key`
5. Click **Enable CORS and replace existing CORS headers**.
6. **Deploy the API** to apply changes.

---

### **B. Manually Adding OPTIONS Method**

1. Create an **OPTIONS method** for the resource.
2. Configure **Mock Integration**.
3. Add **Method Response** headers:

   * `Access-Control-Allow-Origin`
   * `Access-Control-Allow-Methods`
   * `Access-Control-Allow-Headers`
4. In **Integration Response**, map headers to fixed values.
5. Deploy the API.

> ✅ The OPTIONS method responds to **preflight requests** browsers send before actual API calls.

---

### **3️⃣ Using OpenAPI / Terraform / CloudFormation**

* You can define CORS headers in your **API definition** or infrastructure as code.
* Example: set headers in **Method Response** and **Integration Response** for OPTIONS.

---

### **4️⃣ Key Tips**

* Always **deploy** after enabling CORS.
* If using **custom headers or auth tokens**, add them to `Access-Control-Allow-Headers`.
* Test in browser; if you see **CORS errors**, check **allowed origin and headers**.

---
when do we use CORS in API GAteway with what we willl use
We use **CORS (Cross-Origin Resource Sharing)** in **API Gateway** **when a web application (running in a browser) hosted on one domain needs to call an API hosted on a different domain or origin**.

---

### **When to Use CORS**

1. **Web apps accessing APIs from a different domain**

   * Example: Your front-end app is at `https://www.example.com` and your API is at `https://api.example.com`.
   * Without CORS, the browser **blocks the request** due to the same-origin policy.

2. **Single Page Applications (SPA)**

   * React, Angular, Vue apps often run on `localhost` in dev or a domain in production and call an API hosted elsewhere.

3. **Third-party clients**

   * If your API is public and used by clients from other websites.

---

### **What We Use to Enable CORS**

* **In API Gateway:**

  1. **HTTP Headers**:

     * `Access-Control-Allow-Origin` → Which domains can access your API
     * `Access-Control-Allow-Methods` → Allowed methods (GET, POST, etc.)
     * `Access-Control-Allow-Headers` → Allowed request headers
  2. **OPTIONS method (preflight request)**:

     * Browsers send this automatically to check permissions before the actual request.

* **Steps in API Gateway**:

  1. Go to **Resources → Actions → Enable CORS** (console)
  2. Or manually create an **OPTIONS method** with proper headers.
  3. Deploy the API.

---

### **Summary**

* **Use CORS** when your **frontend and backend are on different domains or ports**.
* **We use:** `OPTIONS` method + `Access-Control-*` headers in API Gateway.

---

If you want, I can give a **real-world example with React frontend calling API Gateway** showing exactly where CORS comes into play. Do you want me to do that?

If you want, I can make a **diagram showing how CORS works with OPTIONS and actual request flow in API Gateway**—it’s super helpful for interviews.

Do you want me to do that?

