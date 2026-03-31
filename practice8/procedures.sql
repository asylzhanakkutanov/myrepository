
-- 1. Upsert single contact
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- 2. Upsert multiple users with validation
CREATE OR REPLACE PROCEDURE upsert_multiple_users(
    p_names VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\+7\d{10}$' THEN
            PERFORM upsert_contact(p_names[i], p_phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;

    IF array_length(invalid_data, 1) > 0 THEN
        RAISE NOTICE 'Invalid data: %', array_to_string(invalid_data, ', ');
    END IF;
END;
$$;

-- 3. Delete by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_query VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_query OR phone = p_query;
END;
$$;