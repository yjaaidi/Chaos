Feature: Json validator

    Scenario: wording is required in severity
        When I post to "/severities" with:
        """
        {}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'wording' is a required property  Failed validating 'required' in schema"

        When I post to "/severities" with:
        """
        {"wording": "foo", "priority":"2"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "u'2' is not of type 'integer', 'null'  Failed validating 'type' in schema['properties']['priority']"

    Scenario: wording is required in cause
        When I post to "/causes" with:
        """
        {}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'wording' is a required property  Failed validating 'required' in schema"

    Scenario: name  is required in channel
        When I post to "/channels" with:
        """
        {"max_size": 500, "content_type": "text/type"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'name' is a required property  Failed validating 'required' in schema"

    Scenario: max_size  is required in channel
        When I post to "/channels" with:
        """
        {"name": "sms", "content_type": "text/type"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'max_size' is a required property  Failed validating 'required' in schema"

        When I post to "/channels" with:
        """
        {"name": "sms", "max_size": "20", "content_type": "text/type"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "u'20' is not of type 'integer', 'null'  Failed validating 'type' in schema['properties']['max_size']"

    Scenario: content_type is required in channel
        When I post to "/channels" with:
        """
        {"name": "sms", "max_size": 500}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'content_type' is a required property  Failed validating 'required' in schema"

    Scenario: reference is required in disruption
        Given I post to "/disruptions" with:
        """
        {"note": "hello", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'reference' is a required property  Failed validating 'required' in schema"

    Scenario: cause is required in disruption
        Given I post to "/disruptions" with:
        """
        {"reference": "foo", "note": "hello"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'cause' is a required property  Failed validating 'required' in schema"

    Scenario: severity is required in impcat

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}]}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error" should exist
        And the field "error.message" should be "'severity' is a required property  Failed validating 'required' in schema"
