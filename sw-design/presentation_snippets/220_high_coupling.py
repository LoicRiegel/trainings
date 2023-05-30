def check_email_validity(email):
    if email.header.bearer.invalid():
        raise Exception("Email invalid because the header bearer is invalid")
    if email.header.received != email.header.received.spf:
        raise Exception("Email invalid because received has a mismatch")
    print("Email valid")

# or

def generate_breadcrumbs(location: Location) -> dict[str, str]:
    breadcrumbs: dict[str, str] = {}
    main_url = "https://myapi.com"
    if location.geolocation[0]:
        if location.geolocation[0].postal_code:
            breadcrumbs[
                "postal_code_url"
            ] = f"{main_url}/postal_code/{location.geolocation[0].postal_code}/"
        if location.geolocation[0].city:
            city_slug = location.geolocation[0].city.lower().replace(" ", "-")
            breadcrumbs["city_url"] = f"{main_url}/region/{city_slug}/"
        if location.geolocation[0].province:
            breadcrumbs[
                "province_url"
            ] = f"{main_url}/region/province/{location.geolocation[0].province.lower()}/"
    return breadcrumbs

"""Notes to self:
- check_email_validity is tightly coupled to the email object because it must know about
  very deep information
- generate_breadcrumbs is tightly coupled to
    - the location object
    - the API routes    

"""