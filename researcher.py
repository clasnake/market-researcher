from abc import ABC, abstractmethod

import logging

from models import Company
from ai_providers import BedrockProvider

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Researcher:
    def __init__(self):
        pass

    @abstractmethod
    def find_top_companies(self, company_type: str) -> []:
        """ Use the LLM to find the top companies for the given company type """
        pass

    @abstractmethod
    def get_company_details(self, company_name: str) -> Company:
        """ Use the LLM to get the details for the given company name """
        pass

    @abstractmethod
    def generate_report(self, company_details: []) -> str:
        """ Use the LLM to generate a report for the given company details """
        pass

    def research_for_company_type(self, company_type: str) -> str:
        top_companies = self.find_top_companies(company_type)
        company_details = []
        for company in top_companies:
            company_details.append(self.get_company_details(company))
        report = self.generate_report(company_details)

        return report


class MarketResearcherV1(Researcher):
    def __init__(self):
        self.bedrock_provider = BedrockProvider()

    def find_top_companies(self, company_type: str):
        logger.info(f"Finding top companies for {company_type}")
        prompt = f"Search the web for the top 3 companies involved in {company_type} leveraging AI, return the names in a list"
        response = self.bedrock_provider.converse_with_computer_use(prompt)
        # TODO: Parse response into list of company names
        return ['Company A', 'Company B', 'Company C']

    def get_company_details(self, company_name: str):
        """ TODO: Call LLM, parse results into Company object """
        logger.info(f"Getting company details for {company_name}")
        return Company(name=company_name, description="")

    def generate_report(self, company_details: []):
        """ TODO: Call LLM, parse results into a report """
        logger.info(f"Generating report for {company_details}")
        return "This is the report"
