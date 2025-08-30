# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.x.x   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to [shivjani2005@gmail.com](mailto:shivjani2005@gmail.com) with the subject line "ClassBuddy Security Vulnerability".

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

* Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
* Full paths of source file(s) related to the manifestation of the issue
* The location of the affected source code (tag/branch/commit or direct URL)
* Any special configuration required to reproduce the issue
* Step-by-step instructions to reproduce the issue
* Proof-of-concept or exploit code (if possible)
* Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

## Preferred Languages

We prefer all communications to be in English.

## Security Measures

ClassBuddy implements several security measures:

### Authentication & Authorization

* JWT-based authentication
* OAuth2 with PKCE flow
* Role-based access control (RBAC)
* Secure session management

### Data Protection

* Encryption at rest for sensitive data
* TLS 1.3 for data in transit
* Password hashing with bcrypt
* API rate limiting

### Infrastructure Security

* Container security scanning
* Dependency vulnerability scanning
* OWASP security practices
* Regular security audits

### Mobile Security

* Certificate pinning
* Secure keychain/keystore usage
* Root/jailbreak detection
* Code obfuscation for production builds

## Responsible Disclosure

We ask that you:

1. Give us reasonable time to investigate and mitigate an issue before making any information public
2. Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our services
3. Only interact with accounts you own or with explicit permission of the account holder

## Recognition

We appreciate the security research community and believe that responsible disclosure of security vulnerabilities helps us ensure the security and privacy of all our users.

We will acknowledge your contribution in our security advisories (unless you prefer to remain anonymous).

## Bug Bounty

Currently, we do not have a formal bug bounty program. However, we may provide recognition and small rewards for significant security findings at our discretion.

## Contact

For any questions about this security policy, please contact:

* Email: [shivjani2005@gmail.com](mailto:shivjani2005@gmail.com)
* Project Lead: [@Jani-shiv](https://github.com/Jani-shiv)
