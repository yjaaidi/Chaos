Feature: Create Disruption and impacts

    Scenario: creation of disruption with one impact and localization not exist

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "contributor": "contrib1", "localization":[{"id":"stop_area:AA", "type": "stop_area"}], "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "impacts": [{"severity": {"id": "2ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}]}]}
        """
        Then the status code should be "404"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "ptobject stop_area:AA doesn't exist"

    Scenario: creation of disruption with one impact and ptobject not exist

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "contributor": "contrib1", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}], "objects":[{"id":"stop_area:AA", "type": "stop_area"}]}]}
        """
        Then the status code should be "404"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "ptobject stop_area:AA doesn't exist"

    Scenario: creation of disruption with one impact

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "contributor": "contrib1", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}]}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.impacts.pagination.total_result" should be 1
        And the field "disruption.version" should be 1
        And the field "disruption.impacts.impacts" should have a size of 1
        And the field "disruption.impacts.impacts.0" is valid impact

    Scenario: creation of disruption with one impact and ptobject line_section, metas valid

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "contributor": "contrib1", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}], "objects": [{"id":"line:JDR:M5", "type":"line_section","line_section": {"line":{"id":"line:JDR:M5","type":"line"}, "start_point":{"id":"stop_area:JDR:SA:BASTI", "type":"stop_area"}, "end_point":{"id":"stop_area:JDR:SA:CHVIN", "type":"stop_area"}, "sens":2, "routes":[{"type":"route", "id":"route:JDR:M14"}, {"type":"route", "id":"route:JDR:M1"}], "metas":[{"key":"direction", "value":"1234"}] }}]}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"

    Scenario: creation of disruption with one impact and ptobject line_section, metas invalid

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "contributor": "contrib1", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}], "objects": [{"id":"line:JDR:M5", "type":"line_section","line_section": {"line":{"id":"line:JDR:M5","type":"line"}, "start_point":{"id":"stop_area:JDR:SA:BASTI", "type":"stop_area"}, "end_point":{"id":"stop_area:JDR:SA:CHVIN", "type":"stop_area"}, "sens":2, "routes":[{"type":"route", "id":"route:JDR:M14"}, {"type":"route", "id":"route:JDR:M1"}], "metas":[{"key":"direction"}] }}]}]}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "'value' is a required property"
