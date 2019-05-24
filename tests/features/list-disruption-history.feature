Feature: disruption history
    Background:
        I fill in header "X-Customer-Id" with "5"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "X-Contributors" with "contrib1"
    Scenario: List of an updated disruption
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | cause1    | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
            | cause2    | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7bfab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date | cause_id                              | client_id                            | contributor_id                       |version|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2018-09-11T13:50:00    | 2018-12-31T16:50:00  | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |1|
        Given I have the following history_disruption in my database:
            | id | disruption_id  | data        | created_at          |
            | s408adec-0243-11e6-969b-0050568c8389 | a750994c-01fe-11e4-b4fb-080027079ff3 | {"status": "published", "created_at": "2019-05-24T12:25:02Z", "impacts": [{"created_at": "2019-05-24T12:25:02Z", "updated_at": null, "disruption": {}, "objects": [{"type": "line", "id": "line:DUA:810802061", "name": "A\u00e9roport CDG 2 / Mitry Claye - Robinson / St-R\u00e9my l\u00e8s Chevreuse"}], "id": "f4491f85-7e1e-11e9-a149-f8cab834b8b7", "severity": {"color": "#FF4455", "created_at": "2016-05-31T09:13:36Z", "effect": "significant_delays", "updated_at": null, "priority": 2, "wordings": [{"value": "ralenti", "key": "short"}, {"value": "20 \u00e0 30 minutes suppl\u00e9mentaires de trajet", "key": "long"}, {"value": "20 \u00e0 30 min de trajet en plus", "key": "medium"}], "id": "f4b1eba4-270f-11e6-83cb-005056a47b86", "wording": "20 \u00e0 30 minutes suppl\u00e9mentaires de trajet"}, "messages": [], "send_notifications": true, "notification_date": "2019-05-24T12:25:02Z", "application_period_patterns": [], "application_periods": [{"begin": "2019-05-24T12:20:00Z", "end": "2019-05-24T14:20:00Z"}]}], "reference": "realtime_root-20190524142426", "publication_status": "ongoing", "publication_period": {"begin": "2019-05-24T12:20:00Z", "end": "2019-05-24T14:20:00Z"}, "localization": [], "updated_at": null, "properties": {}, "note": null, "version": 1, "contributor": "shortterm.tr_transilien", "cause": {"category": {"updated_at": "2016-05-31T09:13:36Z", "created_at": "2015-02-05T14:22:56Z", "id": "7a8160fa-ad42-11e4-adc9-005056a47b86", "name": "Trafic inopin\u00e9"}, "updated_at": "2016-05-31T13:09:54Z", "id": "f62cb4a0-270f-11e6-83cb-005056a47b86", "wordings": [{"value": "animal sur la voie", "key": "external_long"}, {"value": "animal sur la voie", "key": "external_short"}, {"value": "__RATP", "key": "internal"}, {"value": "R I animal sur la voie", "key": "external_medium"}], "created_at": "2016-05-31T09:13:38Z"}, "id": "f4491f84-7e1e-11e9-a149-f8cab834b8b7", "tags": []} | 2014-04-02T23:52:12 |
        Given I have the following severities in my database:
            | wording   | color   | created_at          | updated_at          | is_visible | id                                   | client_id                            |
            | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following tags in my database:
            | name      |  created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   |  2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 5ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
            | strike    |  2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 5ffab232-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the relation associate_disruption_tag in my database:
            | tag_id                               | disruption_id                        |
            | 5ffab230-3d48-4eea-aa2c-22f8680230b6 | a750994c-01fe-11e4-b4fb-080027079ff3 |
        Given I have the following properties in my database:
            | created_at          | id                                   | client_id                            | key    | type   |
            | 2014-04-02T23:52:12 | e408adec-0243-11e6-954b-0050568c8382 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | key    | type   |
            | 2014-04-02T23:52:12 | f408adec-0243-11e6-954b-0050568c8382 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | test   | test   |
        Given I have the following ptobject in my database:
            | type     | uri                    | created_at          | updated_at          | id                                         |
            | stop_area| stop_area:JDR:SA:CHVIN | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |
            | stop_area| stop_area:JDR:SA:BASTI | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 2ffab232-3d48-4eea-aa2c-22f8680230b6       |
        Given I have the following associate_disruption_properties in my database:
            | value | disruption_id                        | property_id                          |
            | val1  | a750994c-01fe-11e4-b4fb-080027079ff3 | e408adec-0243-11e6-954b-0050568c8382 |
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3" with:
        """
        {"reference":"foo2", "contributor": "contrib1", "properties":[], "cause":{"id":"7bfab230-3d48-4eea-aa2c-22f8680230b6"},"publication_period":{"begin":"2018-09-11T13:50:00Z","end":"2018-12-31T16:50:00Z"},"impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"objects": [{"id": "network:JDR:1","type": "network"}],"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.version" should be "2"
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3" with:
        """
        {"reference":"foo2", "contributor": "contrib1", "properties":[], "localization":[{"id":"stop_area:JDR:SA:CHVIN", "type":"stop_area"}], "cause":{"id":"7ffab230-3d48-4eea-aa2c-22f8680230b6"},"publication_period":{"begin":"2018-09-15T13:50:00Z","end":"2018-12-31T16:50:00Z"},"impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"objects": [{"id": "network:JDR:1","type": "network"}],"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.version" should be "3"
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3" with:
        """
        {"reference":"foo3", "contributor": "contrib1", "note":"note1", "properties":[{"property_id":"e408adec-0243-11e6-954b-0050568c8382", "value":"val1"},{"property_id":"f408adec-0243-11e6-954b-0050568c8382", "value":"val2"}], "tags":[{"id":"5ffab232-3d48-4eea-aa2c-22f8680230b6"}], "cause":{"id":"7ffab230-3d48-4eea-aa2c-22f8680230b6"},"publication_period":{"begin":"2018-09-15T13:50:00Z","end":"2018-12-31T16:50:00Z"},"impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"objects": [{"id": "network:JDR:1","type": "network"}],"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.version" should be "4"
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3" with:
        """
        {"reference":"foo3", "contributor": "contrib1", "properties":[], "localization":[{"id":"stop_area:JDR:SA:CHVIN", "type":"stop_area"}, {"id":"stop_area:JDR:SA:BASTI", "type":"stop_area"}], "tags":[{"id":"5ffab230-3d48-4eea-aa2c-22f8680230b6"},{"id":"5ffab232-3d48-4eea-aa2c-22f8680230b6"}], "cause":{"id":"7ffab230-3d48-4eea-aa2c-22f8680230b6"},"publication_period":{"begin":"2018-09-15T13:50:00Z","end":"2019-01-10T16:50:00Z"},"impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"objects": [{"id": "network:JDR:1","type": "network"}],"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.version" should be "5"
        When I get "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/history"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 5
        And the field "disruptions.0.reference" should be "foo"
        And the field "disruptions.0.note" should be "hello"
        And the field "disruptions.0.cause.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.0.publication_period.begin" should be "2018-09-11T13:50:00Z"
        And the field "disruptions.0.publication_period.end" should be "2018-12-31T16:50:00Z"
        And the field "disruptions.0.localization" should have a size of 0
        And the field "disruptions.0.properties" should have a size of 1
        And the field "disruptions.0.properties.type.0.property.id" should be "e408adec-0243-11e6-954b-0050568c8382"
        And the field "disruptions.0.properties.type.0.value" should be "val1"
        And the field "disruptions.0.tags" should have a size of 1
        And the field "disruptions.0.tags.0.name" should be "weather"
        And the field "disruptions.0.version" should be "1"
        And the field "disruptions.1.reference" should be "foo2"
        And the field "disruptions.1.note" should be null
        And the field "disruptions.1.cause.id" should be "7bfab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.1.publication_period.begin" should be "2018-09-11T13:50:00Z"
        And the field "disruptions.1.publication_period.end" should be "2018-12-31T16:50:00Z"
        And the field "disruptions.1.properties" should have a size of 0
        And the field "disruptions.1.localization" should have a size of 0
        And the field "disruptions.1.tags" should have a size of 0
        And the field "disruptions.1.version" should be "2"
        And the field "disruptions.2.reference" should be "foo2"
        And the field "disruptions.2.note" should be null
        And the field "disruptions.2.cause.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.2.publication_period.begin" should be "2018-09-15T13:50:00Z"
        And the field "disruptions.2.publication_period.end" should be "2018-12-31T16:50:00Z"
        And the field "disruptions.2.properties" should have a size of 0
        And the field "disruptions.2.localization" should have a size of 1
        And the field "disruptions.2.localization.0.id" should be "stop_area:JDR:SA:CHVIN"
        And the field "disruptions.2.tags" should have a size of 0
        And the field "disruptions.2.version" should be "3"
        And the field "disruptions.3.reference" should be "foo3"
        And the field "disruptions.3.note" should be "note1"
        And the field "disruptions.3.cause.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.3.publication_period.begin" should be "2018-09-15T13:50:00Z"
        And the field "disruptions.3.publication_period.end" should be "2018-12-31T16:50:00Z"
        And the field "disruptions.3.properties" should have a size of 2
        And the field "disruptions.3.properties.type.0.property.id" should be "e408adec-0243-11e6-954b-0050568c8382"
        And the field "disruptions.3.properties.type.0.value" should be "val1"
        And the field "disruptions.3.properties.test.0.property.id" should be "f408adec-0243-11e6-954b-0050568c8382"
        And the field "disruptions.3.properties.test.0.value" should be "val2"
        And the field "disruptions.3.localization" should have a size of 0
        And the field "disruptions.3.tags" should have a size of 1
        And the field "disruptions.3.tags.0.name" should be "strike"
        And the field "disruptions.3.version" should be "4"
        And the field "disruptions.4.reference" should be "foo3"
        And the field "disruptions.4.note" should be null
        And the field "disruptions.4.cause.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.4.publication_period.begin" should be "2018-09-15T13:50:00Z"
        And the field "disruptions.4.publication_period.end" should be "2019-01-10T16:50:00Z"
        And the field "disruptions.4.properties" should have a size of 0
        And the field "disruptions.4.localization" should have a size of 2
        And the field "disruptions.4.tags" should have a size of 2
        And the field "disruptions.4.version" should be "5"
    Scenario: Disruption with ptobject line_section
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following severities in my database:
            | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
            | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following disruptions in my database:
            | reference | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date | cause_id                            | client_id                            | contributor_id                       | version |
            | foo       | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 5ffab230-3d48-4eea-aa2c-22f8680230b6 | 2018-09-11T13:50:00    | 2018-12-31T16:50:00  | 7ffab230-3d48-4eea-aa2c-22f8680230b6| 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 | 1       |
        When I put to "/disruptions/5ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"reference": "foo", "contributor": "contrib1", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}, "publication_period":{"begin":"2018-09-11T13:50:00Z","end":"2018-12-31T16:50:00Z"}, "impacts": [{"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}], "objects": [{"id":"line:JDR:M5", "type":"line_section","line_section": {"line":{"id":"line:JDR:M5","type":"line"}, "start_point":{"id":"stop_area:JDR:SA:BASTI", "type":"stop_area"}, "end_point":{"id":"stop_area:JDR:SA:CHVIN", "type":"stop_area"}, "sens":2, "routes":[{"type":"route", "id":"route:JDR:M14"}, {"type":"route", "id":"route:JDR:M1"}], "metas":[{"key":"direction", "value":"1234"}] }}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        When I get "/disruptions/5ffab230-3d48-4eea-aa2c-22f8680230b6/history"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 2
