DELIMITER $$

DROP PROCEDURE IF EXISTS `usp_{{table}}_i_{{table}}`$$

CREATE PROCEDURE `usp_{{table}}_i_{{table}}`
(
    {% for c in columns if c.Key != 'PRI' %}IN p_{{c.Field}} {{c.Type}}, {% endfor %}
    OUT o_result int
)
BEGIN
    INSERT INTO `{{table}}`
    (
        {% for c in columns if c.Key != 'PRI' %}`{{c.Field}}`{% if not loop.last %},
        {% endif %}{% endfor %}
    )
    VALUES
    (
        {% for c in columns if c.Key != 'PRI' %}p_{{c.Field}}{% if not loop.last %},
        {% endif %}{% endfor %}
    );

    SET o_result = LAST_INSERT_ID();
END$$

DELIMITER ;